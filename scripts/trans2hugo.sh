#!/bin/bash

# Get the absolute path to the directory containing the script
script_dir=$(dirname "$(readlink -f "$0")")

# Get the absolute path to the project root
project_root=$(dirname "$script_dir")

# Read the entire post.sh file into memory
post_content=$(cat "$script_dir/post.sh")

# Create a temporary file in the same directory as post.sh
tmp_file="$script_dir/tmp_post.sh"

# Process each URL
while IFS= read -r url; do
  if [[ "$url" == *"[√]"* ]]; then
    echo "Skipping processed URL: $url"
  else
    # Construct the file path
    filename=$(echo "$url" | sed 's/%/%25/g' | sed 's/ /%20/g' | sed 's/!/%21/g' | sed 's/"/%22/g' | sed 's/#/%23/g' | sed 's/\$/%24/g' | sed 's/&/%26/g' | sed "s/'/%27/g" | sed 's/(/%28/g' | sed 's/)/%29/g' | sed 's/\*/%2A/g' | sed 's/+/%2B/g' | sed 's/,/%2C/g' | sed 's/\//%2F/g' | sed 's/:/%3A/g' | sed 's/;/%3B/g' | sed 's/</%3C/g' | sed 's/=/%3D/g' | sed 's/>/%3E/g' | sed 's/?/%3F/g' | sed 's/@/%40/g')
    file_path="$project_root/content/zh-cn/post/${filename}"

    # Execute the command and check the exit code
    python "$script_dir/trans2hugo.py" "$file_path"
    if [ $? -eq 0 ]; then
      post_content=$(echo "$post_content" | sed "s#$url#[√] $url#g")
    else
      echo "转换失败: $file_path"
    fi
  fi
done < <(echo "$post_content")

# Write the updated content to the temporary file
echo "$post_content" > "$tmp_file"

# Replace the original file with the temporary file
mv "$tmp_file" "$script_dir/post.sh"

echo "Finished 格式转换"
