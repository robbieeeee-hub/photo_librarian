# https://instructobit.com/tutorial/108/How-to-share-global-variables-between-files-in-Python

def initialize():
    global valid_image
    valid_image = 1
    global total_files_reviewed
    total_files_reviewed = 0
    global successful_date_changes
    successful_date_changes = 0

    # path_to_photos = 'Photos/'  # On MaOS

    global path_to_photos
    global path_to_videos
    global path_to_corrupted
    global path_to_other

    path_to_photos = '/home/ubuntu/Samba/Photos/'
    path_to_videos = '/home/ubuntu/Samba/Videos'
    path_to_corrupted = '/home/ubuntu/Samba/Corrupted/'
    path_to_other = '/home/ubuntu/Samba/Other/'