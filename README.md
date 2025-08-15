# random-shapes-art-generator
algorithm that generates art by randomly plotting shapes

![gif](https://github.com/randomoncanvas-art-maker/random-shapes-art-generator/blob/feature/infrastructure/images/sample_animation_seahorse.GIF)

## Overview

## Requirement
- macOS
- docker
- docker-compose
## Usage
clone repository.
```
git clone https://github.com/randomoncanvas-art-maker/random-shapes-art-generator.git
```
build envailment using Docker and docker-compose.
```
cd random-shapes-art-generator/docker
docker compose up -d
docker exec -it sh
```
Run the generator in a docker container.
```
cd main
python main.py --input_file_path ../dataset/sample/bird.jpg --output_dir_path ../output/sample
```
After execution, the results will be output to `output_dir_path`.
## Features

## Reference
- https://note.com/lively_crocus13/n/n721505f6ddbe
## Author

- [Instagram](https://www.instagram.com/random.on.canvas_art?igsh=dTRkaGRwZ3NnNXBo&utm_source=qr)
- [X]()
- Mail:random.on.canvas.art@gmail.com

## Licence

