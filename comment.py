from fastapi import APIRouter, Path 
from model import Comment

comment_router = APIRouter()

comment_list = []
comment_counter = 0

@comment_router.post("/comment")
async def add_comment(comment: Comment) -> dict:
    global comment_counter
    comment.id = comment_counter = comment_counter + 1
    comment_list.append(comment)
    return {
        "msg" : "comment added successfully"
    }

@comment_router.get("/comment")
async def retrieve_comments() -> dict:
    return {
        "comments" : comment_list
    }

@comment_router.get("/comment/{comment_id}")
async def get_single_comment(comment_id: int = Path(..., title = "the ID of the comment to retrieve")) -> dict:
    for comment in comment_list:
        if comment.id == comment_id:
            return { "comment" : comment}
    return {"msg" : "comment with supplied ID doesn't exist"}

@comment_router.delete("/comment/{comment_id}")
async def delete_comment(comment_id: int = Path(..., title="the ID of the todo to delete")) -> dict:
    for index, comment in enumerate(comment_list):
        if comment.id == comment_id:
            del comment_list[index]
            return {"msg": f"Comment with ID {comment_id} deleted sucessfully"}
    return {"msg": "Comment with supplied ID doesn't exist"}
