#import pymongo
#client=pymongo.MongoClient("string url")

#Not a good practice to write id and password in the code files.....
from pymongo import MongoClient
from bson import ObjectId

client=MongoClient("mongodb+srv://<user_name>:<password>@cluster0.y2lzovm.mongodb.net/", tlsAllowInvalidCertificates=True)
db=client["ytmanager"]
video_collection=db["videos"]

# print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name" : name, "time" : time})

def update_video(video_id,new_name,new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name":new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("*" * 70)
        print("YouTube Video Manager -> chose a option below..")
        print("1. List all videos.")
        print("2. Add a video.")
        print("3. Update details of a video.")
        print("4. Delete a video.")
        print("5. Exit.")
        print("*" * 70)

        choice=input("Enter the option : ")

        match choice:
            case '1':
                print("*" * 70)
                list_videos()
                print("*" * 70)

            case '2':
                print("*" * 70)
                name=input("Enter the name of the video : ")
                time=input("Enter the duration of the video: ")
                add_video(name,time)
                print("Video is added successfully.\n")
                print("*" * 70)

            case '3':
                print("*" * 70)
                video_id=input("Enter the id of the video to be updated : ")
                name=input("Enter the new name of the video: ")
                time=input("Enter the new duration of the video: ")
                update_video(video_id,name,time)
                print("Video detail is updated successfully.\n")
                print("*" * 70)

            case '4':
                print("*" * 70)
                video_id=input("Enter video_id to be deleted: ")
                delete_video(video_id)
                print("Video is deleted successfully.\n")
                print("*" * 70)

            case '5':
                break
            case _:
                print("Invalid Choice!")

if __name__=="__main__":
    main()