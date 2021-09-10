import cog

class Predictor(cog.Predictor):
    def setup():
      """Load the model into memory to make running multiple predictions efficient"""
    def predict():
      """Run a single prediction on the model"""
      # will take an audio input file, might also take some text representation of the loop
