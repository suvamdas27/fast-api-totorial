"""FastAPI application with multiple routes and query parameters."""

import json
from fastapi import FastAPI, HTTPException, status
from fastapi import Response

# from fastapi.params import Body
from .payloadModels import Post


app = FastAPI()

with open("postData.json", "r", encoding="utf-8") as postData:
    postData = json.load(postData)


def writePostData(data):
    """Function to write post data back to the JSON file."""

    with open("postData.json", "w", encoding="utf-8") as postFile:
        json.dump(data, postFile, indent=4)


@app.get("/")
def root():
    """Root endpoint that returns a simple message."""

    return {"message": "Hello, World!"}


@app.get("/home")
def home():
    """Endpoint to get all posts."""

    return {"data": postData}


@app.get("/posts", status_code=status.HTTP_200_OK)
async def getPosts(userID: str, postID: str = None):
    # async def getPosts(response: Response, userID: str, postID: str = None):
    """Endpoint to get posts. If post_id is provided, return specific post; otherwise, return all posts."""

    if userID in postData:
        if postID is not None:
            if postID in postData[userID]:
                output = {"data": postData[userID][postID]}
            else:
                # response.status_code = status.HTTP_404_NOT_FOUND
                # output = [{"data": "Post Not Found"}]
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"PostID {postID} Not Found",
                )
        else:
            output = {"data": postData[userID]}
    else:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # output = [{"data": "User Not Found"}]
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User {userID} Not Found"
        )

    return output


# Example of using Body to accept JSON payload for creating a post.
# Uncomment the following code block to use it.
# Using Body to accept JSON payload for creating a post.
# Body is used to parse the request body as JSON without proper schema.
# @app.post("/createPostwithBody")
# def createPostwithBody(payload: dict = Body(...)):
#     """Endpoint to create a new post for a user."""

#     if payload["userID"] in postData:
#         newPostID = str(int(max(postData[payload["userID"]])) + 1)
#         postData[payload["userID"]][newPostID] = {
#             "post_id": newPostID,
#             "title": payload["title"],
#             "content": payload["content"],
#         }
#         writePostData(postData)
#     else:
#         return [{"message": "User Not Found"}]

#     return [{"message": "Post created successfully"}]


@app.post("/posts/{userID}", status_code=status.HTTP_201_CREATED)
async def createPost(userID: str, payload: Post):
    """Endpoint to create a new post for a user."""

    if userID in postData:
        newPostID = str(int(max(postData.get(userID, {}))) + 1)
        postData[userID][newPostID] = payload.model_dump()
        try:
            writePostData(postData)
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error writing to file: {str(e)}"
            ) from e
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {userID} Not Found",
        )

    return {"message": "Post created successfully"}


@app.delete("/posts/{userID}&{postID}", status_code=status.HTTP_204_NO_CONTENT)
async def deletePost(userID: str, postID: str):
    """Endpoint to delete a post for a user."""

    if userID in postData:
        if postID in postData[userID]:
            del postData[userID][postID]
            writePostData(postData)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"PostID {postID} Not Found",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User {userID} Not Found"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{userID}&{postID}", status_code=status.HTTP_200_OK)
async def updatePost(userID: str, postID: str, payload: Post):
    """Endpoint to update a post for a user."""

    if userID in postData:
        if postID in postData[userID]:
            postData[userID][postID].update(payload.model_dump())
            writePostData(postData)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"PostID {postID} Not Found",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User {userID} Not Found"
        )

    return {"message": "Post updated successfully"}


@app.patch("/posts/{userID}&{postID}", status_code=status.HTTP_200_OK)
async def update_item(userID: str, postID: str, payload: Post):
    """Endpoint to partially update a post for a user."""

    if userID in postData:
        if postID in postData[userID]:

            existingPost = postData[userID][postID]
            existingPostModel = Post(**existingPost)
            newPostData = payload.model_dump(exclude_unset=True)
            updatedPost = existingPostModel.model_copy(update=newPostData)
            postData[userID][postID].update(updatedPost.model_dump())
            writePostData(postData)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"PostID {postID} Not Found",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User {userID} Not Found"
        )

    return {"message": "Post updated successfully"}
