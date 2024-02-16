# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased]

### Added

### Changed

### Fixed

### Removed

## [2.0.0] - 2024-02-16

### Added

- Panorama pre-process from [HorizonNet](https://github.com/sunset1995/HorizonNet). (https://github.com/yushiang-demo/DuLa-Net/pull/1)
- Update packages and add `Dockerfile`, `requirements` to freeze versions. (https://github.com/yushiang-demo/DuLa-Net/pull/2)
- Implement api server. (https://github.com/yushiang-demo/DuLa-Net/pull/3)
- Add api endpoints to schedule dula-net tasks. (https://github.com/yushiang-demo/DuLa-Net/pull/5)

### Changed

- Refactor celery worker with callback when task complete. (https://github.com/yushiang-demo/DuLa-Net/pull/7)
- Won't save result to local storage from worker, uses callback body to send data to server. (https://github.com/yushiang-demo/DuLa-Net/pull/8)

### Fixed

### Removed

## [1.0.0] - 2024-01-19

- Fork from [SunDaDenny/DuLa-Net](https://github.com/SunDaDenny/DuLa-Net).


[unreleased]: https://github.com/yushiang-demo/PanoToMesh/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/yushiang-demo/PanoToMesh/releases/tag/v2.0.0
[1.0.0]: https://github.com/yushiang-demo/PanoToMesh/releases/tag/v1.0.0