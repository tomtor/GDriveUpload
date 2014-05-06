DIR="$1"
shift
for i in "$@"
do
  while true; do
    if upload.py -v -d "$DIR" "$i";
    then
      break
    else
      sleep 60
    fi
  done
done
