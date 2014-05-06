PATH=.:$PATH

rm /media/scratch/dump/*dump*

dump -0 -f - /etc | gzip -c | split -b 100M - /media/scratch/dump/swan-etc.dump.gz.
dump -0 -f - /home/tom/src | gzip -c | split -b 100M - /media/scratch/dump/swan-src.dump.gz.
dump -0 -f - /home/tom/bin | gzip -c | split -b 100M - /media/scratch/dump/swan-bin.dump.gz.
dump -0 -f - /home/tom/Desktop | gzip -c | split -b 100M - /media/scratch/dump/swan-desktop.dump.gz.

bupload.sh "etc-src-bin-desktop" /media/scratch/dump/*dump*

echo Done: ; date
