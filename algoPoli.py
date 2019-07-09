#!/usr/bin/python3
# coding=utf-8
import sys
import redDeDelincuencia
from controladorMenu import *
import bibliotecaFuncionesGrafos

sys.setrecursionlimit(10000) # Por default es 999

# Gestiona el menu principal, lleva a cabo los comandos introducidos por consola por el usuario
# Pre: Recibe como parametro una instancia del objeto RedDeDelincuentes
# Post: Mientras el usuario continue instroduciendo comandos, los mismos seran llevados a cabo.
# pone fin a la ejecucion del programa en caso que el usuario introdusca una linea vacia o EOF.
def menuPrincipal(redDelincuencia):
    controladorMenu = ControladorMenu()
    comando, parametros = controladorMenu.controladorMenuPrincipal()
    while (comando != None):

        if (comando == 'min_seguimientos'):     # Mínimos Seguimientos
            origen = parametros[0]
            destino = parametros[1]
            redDelincuencia.minimoSeguimiento(origen, destino)

        elif (comando == 'mas_imp'):            # Delincuentes más importantes   
            cant = int(parametros[0])
            redDelincuencia.mas_imp(cant)

        elif (comando == 'persecucion'):        # Persecución rápida
            agentesEncubiertos = parametros[0].split(",")
            kMasImportantes = int(parametros[1])
            redDelincuencia.persecucion(agentesEncubiertos, kMasImportantes)
            #print(" ")

        elif (comando == 'comunidades'):        # Comunidades
            min_integrantes = int(parametros[0])
            redDelincuencia.comunidades(min_integrantes)

        elif (comando == 'divulgar'):          # Divulgación de rumor 
            delincuente = parametros[0]
            distMax = int(parametros[1])
            redDelincuencia.divulgarRumor(delincuente, distMax)

        elif (comando == 'divulgar_ciclo'):    # Ciclo de largo n
            delincuenteCiclo = parametros[0]
            largoCiclo = int(parametros[1])
            redDelincuencia.divulgar_ciclo(delincuenteCiclo, largoCiclo)

        elif (comando == 'cfc'):               # Componentes Fuertemente Conexas
            redDelincuencia.cfc()
            #print("CFC 1: 0, 620, 978, 381, 178, 203, 125, 967, 984, 761, 720, 655, 975, 745, 222, 523, 617, 163, 976, 65, 315, 709, 133, 266, 335, 995, 828, 1, 689, 619, 168, 651, 589, 22, 173, 880, 614, 875, 455, 685, 944, 273, 690, 687, 113, 640, 297, 464, 596, 151, 577, 961, 2, 535, 586, 91, 14, 362, 120, 965, 3, 161, 406, 385, 794, 658, 228, 429, 750, 6, 169, 696, 462, 256, 837, 734, 675, 882, 604, 612, 4, 618, 428, 738, 214, 126, 236, 74, 457, 241, 289, 857, 467, 562, 308, 497, 605, 475, 5, 510, 783, 262, 357, 507, 443, 565, 317, 90, 548, 463, 48, 924, 805, 183, 634, 338, 7, 322, 849, 274, 33, 812, 379, 320, 401, 813, 985, 374, 70, 176, 351, 195, 846, 209, 595, 802, 636, 102, 158, 484, 981, 908, 728, 855, 145, 239, 773, 785, 327, 10, 522, 51, 189, 28, 79, 726, 767, 249, 807, 276, 561, 631, 678, 42, 306, 8, 646, 526, 16, 564, 296, 349, 717, 771, 283, 951, 218, 652, 46, 201, 479, 913, 868, 525, 947, 550, 9, 784, 956, 418, 95, 864, 482, 346, 337, 474, 910, 313, 918, 804, 789, 592, 903, 255, 34, 537, 970, 942, 587, 184, 468, 410, 930, 307, 934, 179, 803, 494, 490, 389, 83, 101, 394, 328, 416, 196, 11, 452, 52, 333, 411, 233, 350, 671, 615, 447, 825, 13, 777, 489, 594, 270, 53, 432, 202, 668, 206, 180, 62, 21, 17, 938, 801, 213, 175, 706, 919, 149, 18, 988, 824, 891, 731, 162, 425, 41, 98, 12, 933, 287, 44, 94, 471, 397, 340, 354, 76, 495, 514, 684, 198, 139, 778, 599, 833, 889, 940, 704, 417, 569, 574, 842, 19, 818, 515, 654, 665, 566, 146, 923, 546, 756, 461, 330, 834, 559, 955, 245, 444, 815, 597, 793, 746, 841, 254, 874, 877, 391, 722, 89, 902, 348, 637, 867, 387, 759, 798, 234, 164, 170, 946, 511, 291, 661, 737, 904, 673, 853, 31, 816, 188, 57, 579, 498, 493, 663, 710, 850, 580, 458, 208, 325, 943, 483, 536, 633, 152, 373, 513, 488, 288, 679, 772, 905, 142, 576, 240, 20, 982, 43, 659, 485, 207, 994, 141, 64, 107, 438, 117, 808, 292, 402, 50, 974, 705, 382, 952, 446, 781, 84, 230, 109, 639, 220, 181, 500, 716, 210, 873, 552, 583, 968, 221, 87, 926, 542, 912, 632, 894, 922, 979, 472, 284, 582, 648, 763, 787, 980, 243, 422, 353, 23, 760, 404, 836, 736, 758, 368, 751, 118, 575, 859, 377, 954, 962, 844, 36, 551, 85, 539, 390, 454, 939, 257, 724, 752, 332, 323, 769, 347, 543, 88, 524, 786, 290, 983, 998, 797, 282, 610, 606, 927, 37, 61, 69, 915, 503, 138, 137, 426, 449, 888, 796, 870, 165, 878, 477, 29, 826, 56, 318, 660, 676, 835, 621, 143, 140, 298, 502, 992, 492, 775, 788, 316, 259, 281, 312, 30, 682, 481, 795, 749, 997, 735, 920, 727, 155, 766, 871, 414, 544, 487, 890, 24, 93, 518, 258, 602, 496, 925, 681, 123, 252, 901, 822, 779, 625, 369, 211, 896, 356, 578, 725, 451, 194, 232, 302, 780, 339, 25, 200, 431, 442, 366, 154, 96, 572, 860, 972, 753, 719, 708, 326, 334, 423, 116, 393, 27, 415, 858, 343, 748, 884, 182, 277, 714, 560, 450, 235, 59, 553, 294, 740, 63, 473, 111, 847, 662, 205, 669, 832, 703, 765, 911, 800, 92, 299, 187, 227, 150, 693, 380, 112, 134, 945, 396, 160, 324, 371, 504, 770, 999, 885, 407, 105, 990, 358, 364, 702, 607, 643, 268, 948, 304, 545, 929, 987, 603, 478, 547, 567, 167, 645, 372, 609, 32, 77, 538, 420, 108, 314, 667, 309, 295, 73, 359, 966, 231, 573, 694, 424, 75, 395, 265, 581, 823, 342, 263, 136, 519, 122, 893, 809, 97, 319, 630, 433, 843, 806, 755, 135, 127, 104, 698, 100, 790, 67, 862, 445, 831, 585, 251, 774, 376, 301, 121, 505, 58, 459, 480, 892, 367, 171, 352, 616, 534, 439, 641, 729, 638, 341, 754, 248, 434, 375, 516, 399, 199, 686, 921, 960, 949, 906, 935, 700, 153, 35, 448, 244, 644, 110, 628, 677, 217, 883, 186, 531, 653, 215, 272, 932, 413, 521, 764, 26, 528, 819, 741, 886, 39, 300, 971, 250, 237, 278, 329, 68, 876, 747, 247, 811, 533, 791, 649, 590, 460, 664, 40, 115, 177, 344, 814, 712, 331, 881, 776, 469, 466, 670, 355, 739, 792, 556, 303, 937, 744, 132, 917, 128, 419, 129, 591, 185, 711, 721, 131, 260, 865, 192, 476, 392, 47, 144, 916, 666, 78, 928, 718, 688, 361, 839, 435, 953, 627, 730, 964, 197, 680, 656, 229, 264, 563, 866, 119, 977, 193, 969, 701, 959, 440, 360, 757, 957, 991, 99, 931, 626, 854, 38, 508, 593, 386, 384, 246, 914, 305, 86, 568, 106, 403, 398, 530, 557, 817, 269, 216, 683, 549, 900, 286, 829, 827, 613, 82, 762, 907, 54, 691, 973, 989, 280, 697, 707, 821, 311, 768, 405, 81, 963, 293, 872, 887, 400, 742, 529, 993, 909, 271, 950, 895, 695, 897, 941, 650, 159, 986, 310, 509, 60, 588, 601, 321, 852, 378, 124, 409, 558, 782, 45, 72, 996, 279, 600, 635, 647, 512, 80, 147, 840, 427, 517, 856, 713, 219, 267, 190, 421, 172, 598, 674, 623, 624, 156, 114, 191, 365, 470, 408, 838, 506, 554, 453, 540, 204, 863, 388, 55, 285, 642, 383, 456, 799, 723, 743, 861, 225, 898, 715, 692, 223, 845, 336, 629, 157, 869, 699, 501, 584, 622, 958, 412, 830, 226, 672, 657, 541, 224, 166, 936, 570, 520, 555, 238, 345, 733, 527, 499, 848, 275, 820, 441, 253, 465, 174, 611, 261, 430, 242, 608, 66, 148, 437, 491, 71, 436, 532, 49, 130, 851, 899, 15, 732, 212, 103, 363, 370, 571, 810, 486, 879")

        try:
            comando, parametros = controladorMenu.controladorMenuPrincipal()
        except EOFError:
            comando = None

# Recibe como argumento la ruta del archivo .tsv que contiene las comunicaciones
def main(argv):
    if(len(argv) != 1):
        print("Error: Cantidad erronea de parametros")
        return -1
    try:
        # Intancia de Clases
        grafo = bibliotecaFuncionesGrafos.cargarGrafo(argv[0])
        redDeDelincuentes = redDeDelincuencia.RedDeDelincuentes(grafo)
        # Llamado a Menu Principal
        menuPrincipal(redDeDelincuentes)
        return 0
    except FileNotFoundError:
        print("Error: archivo fuente inaccesible")
        return -1




# Bloque Principal
main(sys.argv[1:])
