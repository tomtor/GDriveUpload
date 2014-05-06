for i in "$@"
do
  while true; do
    if upload.py -v "$i";
    then
      break
    else
      sleep 60
    fi
  done
done
