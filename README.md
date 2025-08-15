# random-shapes-art-generator
algorithm that generates art by randomly plotting shapes

![gif](https://github.com/randomoncanvas-art-maker/random-shapes-art-generator/blob/feature/infrastructure/images/sample_animation_seahorse.GIF)

## Overview
This code can generate a desired image by randomly placing shapes.
Because it is generated randomly, the same image will never be created twice, making it unique.

## Requirement
- macOS
- docker
- docker-compose

## Usage
Clone repository
```
git clone https://github.com/randomoncanvas-art-maker/random-shapes-art-generator.git
```
Build envailment using Docker and docker-compose
```
cd random-shapes-art-generator/docker
docker compose up -d
docker exec -it sh
```
Run the generator in a docker container
```
cd main
python main.py --input_file_path ../dataset/sample/seahorse.jpg --output_dir_path ../output/sample
```
After execution, the results will be output to `output_dir_path`

You can generate any random art by changing the input image.

## Reference
- https://note.com/lively_crocus13/n/n721505f6ddbe

## Author
- [Instagram](https://www.instagram.com/random.on.canvas_art?igsh=dTRkaGRwZ3NnNXBo&utm_source=qr)
- [X](https://x.com/randomoncanvas?s=21&t=FNt_GNO6GCVhZ_ytUxNxKw)
- Mail:random.on.canvas.art@gmail.com

## Licence

