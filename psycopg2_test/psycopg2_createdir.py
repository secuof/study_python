import psycopg2
import os


# # Connect to the DB
# con = psycopg2.connect(
#     host = "192.168.1.226",
#     database = "clarity",
#     user = "clarity",
#     password = "clarity"
# )

# # Cursor
# cur = con.cursor()

# # Excute query and fetchall
# cur.execute("select package, version, checksum from processed limit 10")
# rows = cur.fetchall()

# for r in rows:
#     print(f"id : {r[0]} || name : {r[1]} || test = {r[2]}")

# # Close the cursor
# cur.close()
# # Close the connection
# con.close()


YOUR_DIRECTORY_NAME = "./test"
os.makedirs(os.path.join({YOUR_DIRECTORY_NAME}))

## Create Directory (https://cinema4dr12.tistory.com/1296)
# try:
#     if not(os.path.isdir({YOUR_DIRECTORY_NAME})):
#         os.makedirs(os.path.join({YOUR_DIRECTORY_NAME}))
# except OSError as e:
#     if e.errno != errno.EEXIST:
#         print("Failed to create directory!!!!!")
#         raise

# ## Create File
# import os
 
# filepath = os.path.join({YOUR_FILE_PATH}, "test.txt")
# fid = open(filepath, "w")

# if not os.path.isfile(filepath):
#     fid.write("Text file creation example.")
 
# fid.close()
