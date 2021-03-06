from torch import nn, optim
import torchvision

# a = torch.tensor([2.,3.], requires_grad=True)
# b = torch.tensor([6.,4.], requires_grad=True)
# 
# Q = 3*a**3 - b**2
# 
# external_grad = torch.tensor([1., 1.])
# Q.backward(gradient=external_grad)
# 
# print(9*a**2 == a.grad)
# print(-2*b == b.grad)

# x = torch.rand(5,5)
# y = torch.rand(5,5)
# z = torch.rand((5,5), requires_grad=True)
# 
# a = x+y
# print(f"Does 'a' require gradients? : {a.requires_grad}")
# 
# b = x+z
# print(f"Does 'b' require gradients? : {b.requires_grad}")

model = torchvision.models.resnet18(pretrained=True)

for param in model.parameters():
    param.requires_grad = False

model.fc = nn.Linear(512,10)

optimizer = optim.SGD(model.fc.parameters(), lr=1e-2, momentum=0.9)
