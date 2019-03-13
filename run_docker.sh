docker run -it --rm \
	-v /data:/data \
	-p 127.0.0.1:27017:27017 \
	--network host \
	--name crawler \
	jjanzic/docker-python3-opencv:contrib-opencv-4.0.1 \
	bash
