import torch
import torch.nn as nn

INPUT_FEATURES = 2
OUTPUT_NEURONS = 1

activation = nn.Tanh()

# nn.Moduleクラスから継承している
# やることは、全結合層を最初から実装したニューラルネットワークを出力すること
class NeuralNetwork(nn.Module):
  def __init__(self):
    # super(parent class name, )
    super(NeuralNetwork, self).__init__()
    self.layer1 = nn.Linear(
      INPUT_FEATURES,
      OUTPUT_NEURONS
    )

    def forward(self, input):
      output = activation(self.layer1(input))
      return output

weight_array = nn.parameter(
  torch.tensor([[0.6, -0.2]])
)

bias_array = nn.Parameter(
  torch.tensor([0.8])
)

model.layer1.weight = weight_array
model.layer1.bias = bias_array

params = model.state_dict()

model = NeuralNetwork()
print(model)
print(params)
