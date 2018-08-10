file_path=$(mysql --login-path=myroot -D wordpress -N -e "SELECT SUBSTRING_INDEX(file_path,'.',1) FROM wp_uploaded_video WHERE status='delete';")
for file in $file_path
do
video=$file".mp4"
thumbnail=$file".png"
sudo rm -f $video
sudo rm -f $thumbnail
done

