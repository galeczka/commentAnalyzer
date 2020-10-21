from model import CommentModel
from model import create

create()

model = CommentModel()
model.load()
res = model.predict(["amazing hot✨✨✨❤️❤️", "nice", "Summer is here in Colorado now"])
print(res)
# [1,1,0]