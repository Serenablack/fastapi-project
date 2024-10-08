from fastapi import APIRouter, HTTPException

from socialmediaapi.models.post import (
    Comment,
    CommentIn,
    UserPost,
    UserPostIn,
    userPostwithComments,
)

router = APIRouter()

post_table = {}
comment_table = {}


@router.get("/", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())


@router.post("/", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.model_dump()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post


def find_post(post_id: int):
    return post_table.get(post_id)


@router.get("/post/{id}/comment", response_model=list[Comment])
async def get_comment_for_post(id: int):
    return [comment for comment in comment_table.values() if comment["post_id"] == id]


@router.post("/comment", response_model=Comment, status_code=201)
async def create_comment(comment: CommentIn):
    post = find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, message="Post not found")
    data = comment.model_dump()
    last_record_id = len(comment_table)
    new_comment = {**data, "id": last_record_id}
    comment_table[last_record_id] = new_comment
    return new_comment


@router.get("/post/{id}", response_model=userPostwithComments)
async def get_post_with_comments(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=404, message="Post not found")
    return {"post": post, "comments": await get_comment_for_post(id)}
