from Mods.production_line import Production_line
from cv2 import cv2
from argparse import ArgumentParser


def receive_arguments():
    parser = ArgumentParser(
        description='Podaj ścieżke do obrazu w parametrze --filepath [ścieżka] zmieniony obraz będzie dostępny w lokalizacji projektu o nazwie changed.jpg')

    parser.add_argument('--filepath', dest='filepath', type=str,
                        required=True, help="ścieżka do pliku który chcesz zaimportować")

    args = parser.parse_args()
    filepath = args.filepath
    return filepath


def main():
    image = cv2.imread(receive_arguments())
    prd1 = Production_line(image)
    prd1.add_step(10)

    # prd1 = Production("Zaczynam produkcje:")
    # prd1.add_step(3)


if __name__ == '__main__':
    main()
