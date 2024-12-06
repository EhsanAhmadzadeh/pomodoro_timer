
# Pomodoro Timer CLI Application

A simple command-line Pomodoro timer application written in Python.

## Features

- Customizable work and break durations
- Pause and resume functionality
- Desktop notifications upon session completion
- Cross-platform support
- Colored terminal output for better readability

## Installation

### Prerequisites

- Python 3.6 or higher
- pip

### Install via pip

```
pip install pomodoro_timer
```

### Install from source

1. Clone the repository:

```
git clone https://github.com/EhsanAhmadzadeh/pomodoro_timer.git
```

2. Navigate to the project directory:

```
cd pomodoro_timer
```

3. Install the package:

```
pip install .
```

## Usage

```
pomodoro --work 25 --short_break 5 --long_break 15
```

### Options

- `-w`, `--work`: Work duration in minutes (default: 25)
- `-s`, `--short_break`: Short break duration in minutes (default: 5)
- `-l`, `--long_break`: Long break duration in minutes (default: 15)

## Example

Start a Pomodoro session with default durations:

```
pomodoro
```

Start a session with custom durations:

```
pomodoro -w 50 -s 10 -l 30
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: Ehsan Ahmadzadeh
- **Email**: amirehsansolout@gmail.com
