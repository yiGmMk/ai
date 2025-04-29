#!bin/sh

script_dir=$(dirname "$(readlink -f "$0")")
project_root=$(dirname "$script_dir")

echo $script_dir $project_root

# 输出今天新创建的文件
find "$project_root/content/zh-cn/post" -type f -ctime 0 -name "*.md" | while read file; do
  # 获取文件名
  filename=$(basename "$file")
  # 获取文件路径
  filepath=$(dirname "$file")
  # 获取文件的绝对路径
  abs_filepath=$(realpath "$file")
  # 获取文件的相对路径
  rel_filepath=$(realpath --relative-to="$project_root" "$file")
  
  # 输出文件名和路径
  echo "$filename"
#   echo "Path: $filepath"
#   echo "Absolute Path: $abs_filepath"
#   echo "Relative Path: $rel_filepath"
done