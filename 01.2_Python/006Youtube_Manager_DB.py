import sqlite3
conn=sqlite3.connect("vodeos.db")
cursor=conn.cursor()
cursor.execute("""
    Create table if not exists Youtube_Manager(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
""")

def list_video():
    print("*" * 70)
    cursor.execute('select * from Youtube_Manager')
    for row in cursor.fetchall():
        print(row)
    print("*" * 70)

def add_video(name,time):
    cursor.execute('insert into Youtube_Manager(name,time) values( ? , ? ) ', (name,time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute('update Youtube_Manager set name=?,time=? where id=?', (new_name, new_time,video_id))
    conn.commit()
    
def delete_video(video_id):
    cursor.execute('delete from Youtube_Manager where id=?', (video_id,))
    conn.commit()

def main():
    pass

    while True:
        print("\n Youtube Video Manager => Chose the option below: ")
        print("1. List all videos.")
        print("2. Add any video.")
        print("3. Update details of video.")
        print("4. Delete any video.")
        print("5. Exit.")

        choice=input("Enter your choice to execute : ")

        match choice:
            case '1':
                list_video()
            case '2':
                name=input("Enter name of the video: ")
                time=input("Enter duration of the video: ")
                add_video(name,time)
                print("Video added successfully.")
            case '3':
                video_id=int(input("Enter video id to be updated: "))
                name=input("Enter new_name of the video: ")
                time=input("Enter new_duration of the video: ")
                update_video(video_id, name , time)
                print("video updation is successful.")
            case '4':
                video_id=int(input("Enter video id to be deleted: "))
                delete_video(video_id)
                print("The requested video delete is successful.")
            case '5':
                break
            case _:
                print("Invalid choice !")

    conn.close()
if __name__=='__main__':
    main()
