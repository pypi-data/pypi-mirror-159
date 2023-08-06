# Copyright (C) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in project root for information.


import sys
if sys.version >= '3':
    basestring = str

from pyspark import SparkContext, SQLContext
from pyspark.sql import DataFrame
from pyspark.ml.param.shared import *
from pyspark import keyword_only
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from synapse.ml.core.serialize.java_params_patch import *
from pyspark.ml.wrapper import JavaTransformer, JavaEstimator, JavaModel
from pyspark.ml.evaluation import JavaEvaluator
from pyspark.ml.common import inherit_doc
from synapse.ml.core.schema.Utils import *
from pyspark.ml.param import TypeConverters
from synapse.ml.core.schema.TypeConversionUtils import generateTypeConverter, complexTypeConverter


@inherit_doc
class TextLIME(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        inputCol (str): The name of the input column
        model (object): Model to try to locally approximate
        nSamples (int): The number of samples to generate
        outputCol (str): The name of the output column
        predictionCol (str): prediction column name
        regularization (float): regularization param for the lasso
        samplingFraction (float): The fraction of superpixels to keep on
        tokenCol (str): The column holding the token
    """

    inputCol = Param(Params._dummy(), "inputCol", "The name of the input column", typeConverter=TypeConverters.toString)
    
    model = Param(Params._dummy(), "model", "Model to try to locally approximate")
    
    nSamples = Param(Params._dummy(), "nSamples", "The number of samples to generate", typeConverter=TypeConverters.toInt)
    
    outputCol = Param(Params._dummy(), "outputCol", "The name of the output column", typeConverter=TypeConverters.toString)
    
    predictionCol = Param(Params._dummy(), "predictionCol", "prediction column name", typeConverter=TypeConverters.toString)
    
    regularization = Param(Params._dummy(), "regularization", "regularization param for the lasso", typeConverter=TypeConverters.toFloat)
    
    samplingFraction = Param(Params._dummy(), "samplingFraction", "The fraction of superpixels to keep on", typeConverter=TypeConverters.toFloat)
    
    tokenCol = Param(Params._dummy(), "tokenCol", "The column holding the token", typeConverter=TypeConverters.toString)

    
    @keyword_only
    def __init__(
        self,
        java_obj=None,
        inputCol=None,
        model=None,
        nSamples=1000,
        outputCol=None,
        predictionCol="prediction",
        regularization=0.0,
        samplingFraction=0.3,
        tokenCol=None
        ):
        super(TextLIME, self).__init__()
        if java_obj is None:
            self._java_obj = self._new_java_obj("com.microsoft.azure.synapse.ml.lime.TextLIME", self.uid)
        else:
            self._java_obj = java_obj
        self._setDefault(nSamples=1000)
        self._setDefault(predictionCol="prediction")
        self._setDefault(regularization=0.0)
        self._setDefault(samplingFraction=0.3)
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
    
        if java_obj is None:
            for k,v in kwargs.items():
                if v is not None:
                    getattr(self, "set" + k[0].upper() + k[1:])(v)

    @keyword_only
    def setParams(
        self,
        inputCol=None,
        model=None,
        nSamples=1000,
        outputCol=None,
        predictionCol="prediction",
        regularization=0.0,
        samplingFraction=0.3,
        tokenCol=None
        ):
        """
        Set the (keyword only) parameters
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.azure.synapse.ml.lime.TextLIME"

    @staticmethod
    def _from_java(java_stage):
        module_name=TextLIME.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".TextLIME"
        return from_java(java_stage, module_name)

    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
        self._set(inputCol=value)
        return self
    
    def setModel(self, value):
        """
        Args:
            model: Model to try to locally approximate
        """
        self._set(model=value)
        return self
    
    def setNSamples(self, value):
        """
        Args:
            nSamples: The number of samples to generate
        """
        self._set(nSamples=value)
        return self
    
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
        self._set(outputCol=value)
        return self
    
    def setPredictionCol(self, value):
        """
        Args:
            predictionCol: prediction column name
        """
        self._set(predictionCol=value)
        return self
    
    def setRegularization(self, value):
        """
        Args:
            regularization: regularization param for the lasso
        """
        self._set(regularization=value)
        return self
    
    def setSamplingFraction(self, value):
        """
        Args:
            samplingFraction: The fraction of superpixels to keep on
        """
        self._set(samplingFraction=value)
        return self
    
    def setTokenCol(self, value):
        """
        Args:
            tokenCol: The column holding the token
        """
        self._set(tokenCol=value)
        return self

    
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
        return self.getOrDefault(self.inputCol)
    
    
    def getModel(self):
        """
        Returns:
            model: Model to try to locally approximate
        """
        return JavaParams._from_java(self._java_obj.getModel())
    
    
    def getNSamples(self):
        """
        Returns:
            nSamples: The number of samples to generate
        """
        return self.getOrDefault(self.nSamples)
    
    
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
        return self.getOrDefault(self.outputCol)
    
    
    def getPredictionCol(self):
        """
        Returns:
            predictionCol: prediction column name
        """
        return self.getOrDefault(self.predictionCol)
    
    
    def getRegularization(self):
        """
        Returns:
            regularization: regularization param for the lasso
        """
        return self.getOrDefault(self.regularization)
    
    
    def getSamplingFraction(self):
        """
        Returns:
            samplingFraction: The fraction of superpixels to keep on
        """
        return self.getOrDefault(self.samplingFraction)
    
    
    def getTokenCol(self):
        """
        Returns:
            tokenCol: The column holding the token
        """
        return self.getOrDefault(self.tokenCol)

    

    
        