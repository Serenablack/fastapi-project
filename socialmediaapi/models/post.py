from pydantic import BaseModel


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int


class CommentIn(BaseModel):
    comment: str
    post_id: int


class Comment(CommentIn):
    id: int


class userPostwithComments(BaseModel):
    post: UserPost
    comments: list[Comment]
