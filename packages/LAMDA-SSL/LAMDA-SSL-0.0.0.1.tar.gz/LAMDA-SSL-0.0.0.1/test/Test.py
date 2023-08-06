# import numbers
#
# a=1.1
# print(type(a))
# print(isinstance(a,numbers.Number))
#
# import torch
# a=torch.Tensor()
# b=torch.rand(2,3,4)
# a=torch.cat((a,b),dim=0)
# print(a)
# for item in a:
#     print(item.size())

# import sys
# print(sys.path)
# import numpy as np
#
# import torch
# print([(1,2,3)])
# print([1,2,3]+[4]+[234])
# print((1,2,3)[:2]+[4])
# print(torch.Tensor([1]))
# x=np.array([[1,3,2],
#            [1,3,2]])
# # x=np.expand_dims(x,axis=0)
#
# result=x.dot(x.T).dot(x)
#
# print(result)
# import torch
# from torch.nn.modules import EmbeddingBag
#
# # a='21213'
# # print(type(a))
#
# a=torch.Tensor([1,2,3,4,5,6])
# b=torch.Tensor([1,1,1])
# print(torch.cat([a,b]))
# from LAMDA_SSL.Transform.Tokenizer import Tokenizer
# tokenizer=Tokenizer('basic_english',language='en')
# # counter.update(["I", "am", "a", "studnt","!","You are not!"])
# print(tokenizer.fit_transform("You are not!"))
# import numpy as np
# a=np.array([2,2,3])
#
# print(a.all())
# a=['aaa','bbb','vvv']
# print(a[0])
# print(' '.join(a))
# import nltk
# nltk.download('wordnet')
# import numpy as np
#
# a=np.array([1,2,3,4])
# print(np.zeros(20,dtype=int))
# print(len(a))
# import numpy as np
# #
# # a=np.zeros(2,dtype=float)
# # b=np.zeros(2,dtype=int)
# # print(a[0]==b[0])
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# print(a*b)
# print(a[[0,2]])
import torch
import numpy
a=torch.Tensor([1]).numpy()
print(a.min())