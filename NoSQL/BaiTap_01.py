from pymongo import MongoClient
from datetime import datetime


# Buoc 1: Ket noi den MongoDB
client = MongoClient("mongodb://Localhost:27017/")
db = client["tiktokABC"]  #Chon co so du lieu tiktok
# Xoa csdl
client.drop_database("tiktokABC")
# Buoc 2: Tao collections
users_collection = db["users"]
videos_collection = db["videos"]

# Bước 3: Thêm dữ liệu người dùng
users_data = [
    { 'user_id': 1, 'username': 'user1', 'full_name': 'Nguyen Van A', 'followers': 1500, 'following': 200 },
    { 'user_id': 2, 'username': 'user2', 'full_name': 'Tran Thi B', 'followers': 2000, 'following': 300 },
    { 'user_id': 3, 'username': 'user3', 'full_name': 'Le Van C', 'followers': 500, 'following': 100 }
]
users_collection.insert_many(users_data)  # Thêm dữ liệu người dùng

# Bước 4: Thêm dữ liệu video
videos_data = [
    { 'video_id': 1, 'user_id': 1, 'title': 'Video 1', 'views': 10000, 'likes': 500, 'created_at': datetime(2024, 1, 1) },
    { 'video_id': 2, 'user_id': 2, 'title': 'Video 2', 'views': 20000, 'likes': 1500, 'created_at': datetime(2024, 1, 5) },
    { 'video_id': 3, 'user_id': 3, 'title': 'Video 3', 'views': 5000, 'likes': 200, 'created_at': datetime(2024, 1, 10) }
]
videos_collection.insert_many(videos_data)  # Thêm dữ liệu video

# Buoc 5: Truy van du lieu
# 5.1 Xem tat ca nguoi dung
print("Tat ca nguoi dung")
# for user in users_collection.find():
#     print(user)

# 5.2 Tim video co nhieu nguoi xem nhat
# mosted_viewed_video = videos_collection.find().sort("views",-1).limit(1)

print("Nguoi dung co Video co nhieu luot xem nhat")
# for user in mosted_viewed_video:
#     print(user)

# 5.3 Tim tat ca Video cua nguoi dung co username la "user1"
user_videos = videos_collection.find({"user_id":1})
# for video in user_videos:
#     print(video) 
    
# print(video)