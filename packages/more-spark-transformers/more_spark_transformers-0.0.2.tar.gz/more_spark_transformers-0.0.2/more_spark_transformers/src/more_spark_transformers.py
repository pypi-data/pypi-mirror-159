import numpy as np
import pyspark.sql.types as T
import pyspark.sql.functions as F
from pyspark import keyword_only
from pyspark.sql.functions import window, col, rand, last
from pyspark.ml import Transformer
from pyspark.ml.param.shared import HasInputCols, HasOutputCol, Param, Params, TypeConverters
from pyspark.ml.util import DefaultParamsReadable, DefaultParamsWritable


class FFTTransformer(Transformer, HasInputCols, HasOutputCol, DefaultParamsReadable, DefaultParamsWritable):
    inputCols = Param(Params._dummy(), "inputCols", "inputCols", typeConverter=TypeConverters.toListString)
    windowDuration = Param(Params._dummy(), "windowDuration", "windowDuration", typeConverter=TypeConverters.toFloat)
    windowSlideDuration = Param(Params._dummy(), "windowSlideDuration", "windowSlideDuration", typeConverter=TypeConverters.toFloat)
    samplingPeriod = Param(Params._dummy(), "samplingPeriod", "samplingPeriod", typeConverter=TypeConverters.toFloat)
    partitionColumn = Param(Params._dummy(), "partitionColumn", "partitionColumn", typeConverter=TypeConverters.toString)
    timestampColumn = Param(Params._dummy(), "timestampColumn", "timestampColumn", typeConverter=TypeConverters.toString)
    outputCol = Param(Params._dummy(), "outputCol", "outputCol", typeConverter=TypeConverters.toString)

    @keyword_only
    def __init__(
        self,
        inputCols=[], 
        windowDuration=None, 
        windowSlideDuration=None, 
        samplingPeriod=None,
        partitionColumn=None,
        timestampColumn=None,
        outputCol=None
    ):
        super(FFTTransformer, self).__init__()
        kwargs = self._input_kwargs
        self.set_params(**kwargs)

        self.uid = 'FFTTransformer'

        self.fft_udf = F.udf(lambda z: [float(i) for i in np.fft.fft(z)], T.ArrayType(T.FloatType()))

  
    @keyword_only
    def set_params(self, **kwargs):
        self._set(**kwargs)
    

    def _transform(self, dataset):
        df = dataset\
            .groupBy(self.getOrDefault("partitionColumn"), window(self.getOrDefault("timestampColumn"), windowDuration=f'{round(1000 * self.getOrDefault("windowDuration"))} milliseconds', slideDuration=f'{round(1000 * self.getOrDefault("windowSlideDuration"))} milliseconds'))\
            .agg(
                *[self.fft_udf(F.collect_list(col(column))).alias(f"{column}_FFT") for column in self.getOrDefault("inputCols")],
                last(col(self.getOrDefault("outputCol")))
            )\
            .orderBy(rand())
        windowSize = round(1 / self.getOrDefault("samplingPeriod") * self.getOrDefault("windowDuration"))
        df = df\
            .select('*', *[df[f"{column}_FFT"][index] for column in self.getOrDefault("inputCols") for index in range(windowSize) ])\
            .drop(*[f"{column}_FFT" for column in self.getOrDefault("inputCols") ])
        return df
