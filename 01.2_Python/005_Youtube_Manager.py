#Project Name: Youtube_Manager
import json

#Different Methods
#loading data .... method
def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)
        


#list all youtube videos ... method
def list_all_videos(videos):
    # for index, video in enumerate(videos,start=1):
    #     print(f"{index}.{video}")
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}.{video['name']} - {video['time']}")
    print("*" * 70)

#Add a yoytube video ... method
def add_videos(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({'name' : name, 'time' : time})
    save_data_helper(videos)

#update youtube video details ... method
def update_videos_details(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number you want to update: "))
    if 1<=index<=len(videos):
        name=input("Enter the new name of the video: ")
        time=input("Enter the new duration of the video: ")
        videos[index-1]={"name":name,"time":time}
        save_data_helper(videos)
        print("Video details updated successfully")
    else:
        print("Invalid index of the video!")

#delete a youtube videos ... method
def delete_videos(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number you want to delete: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("video number {index} is deleted successfully")
    else:
        print("Invalid index of the video!")
    


#Main Process....
def main():
    videos=load_data()
    while True:
        print("\n Youtube_Manager -> Choose a option")
        print("1. List all youtube video ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice=input("Enter you choice : ")

        match choice:
            case '1':
                list_all_videos(videos)

            case '2':
                add_videos(videos)
            case '3':
                print("3")
                update_videos_details(videos)
            case '4':
                print("4")
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid Option !")

if __name__=="__main__":
    main()