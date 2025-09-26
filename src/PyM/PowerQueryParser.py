# Generated from src/PyM/PowerQueryParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,72,720,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,2,72,
        7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,78,7,78,
        2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,84,2,85,
        7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,91,7,91,
        2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,97,2,98,
        7,98,2,99,7,99,2,100,7,100,2,101,7,101,1,0,1,0,3,0,207,8,0,1,1,1,
        1,1,2,3,2,212,8,2,1,2,1,2,1,2,1,2,3,2,218,8,2,1,3,1,3,1,4,1,4,3,
        4,224,8,4,1,5,3,5,227,8,5,1,5,3,5,230,8,5,1,5,1,5,1,5,1,5,1,5,1,
        6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,248,8,8,1,9,1,9,1,
        9,5,9,253,8,9,10,9,12,9,256,9,9,1,10,1,10,1,10,5,10,261,8,10,10,
        10,12,10,264,9,10,1,11,1,11,1,11,3,11,269,8,11,1,12,3,12,272,8,12,
        1,12,1,12,1,13,1,13,1,13,5,13,279,8,13,10,13,12,13,282,9,13,1,14,
        1,14,1,14,5,14,287,8,14,10,14,12,14,290,9,14,1,15,1,15,1,15,5,15,
        295,8,15,10,15,12,15,298,9,15,1,16,1,16,1,16,5,16,303,8,16,10,16,
        12,16,306,9,16,1,17,1,17,1,17,5,17,311,8,17,10,17,12,17,314,9,17,
        1,18,1,18,1,18,5,18,319,8,18,10,18,12,18,322,9,18,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,3,19,331,8,19,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,3,20,341,8,20,1,20,1,20,3,20,345,8,20,1,20,5,20,348,8,
        20,10,20,12,20,351,9,20,1,20,1,20,1,20,3,20,356,8,20,1,21,1,21,1,
        21,1,21,1,21,1,21,3,21,364,8,21,1,22,1,22,1,23,1,23,1,24,1,24,3,
        24,372,8,24,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,
        28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,30,1,30,3,30,394,8,30,1,
        31,1,31,3,31,398,8,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,3,32,407,
        8,32,1,33,1,33,1,33,1,33,1,33,3,33,414,8,33,1,34,1,34,3,34,418,8,
        34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,3,35,427,8,35,1,36,1,36,1,
        36,1,36,1,37,1,37,1,38,1,38,1,39,1,39,3,39,439,8,39,1,40,1,40,1,
        40,1,40,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,43,1,43,1,43,1,43,1,
        44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,3,45,466,8,45,1,
        46,1,46,3,46,470,8,46,1,47,1,47,3,47,474,8,47,1,47,1,47,3,47,478,
        8,47,1,47,1,47,1,47,1,48,1,48,1,49,1,49,1,49,1,49,1,49,3,49,490,
        8,49,1,50,1,50,1,50,1,50,1,50,3,50,497,8,50,1,51,1,51,3,51,501,8,
        51,1,52,1,52,1,53,1,53,1,54,1,54,1,55,1,55,1,55,1,56,1,56,1,56,1,
        56,1,56,3,56,517,8,56,1,57,1,57,1,57,1,58,1,58,1,58,1,59,1,59,1,
        60,1,60,1,60,1,60,1,60,1,61,1,61,1,61,1,61,1,61,3,61,537,8,61,1,
        62,1,62,1,62,1,62,1,63,1,63,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,
        65,1,65,1,66,1,66,1,67,1,67,1,68,1,68,1,68,3,68,561,8,68,1,69,1,
        69,3,69,565,8,69,1,70,1,70,1,70,1,70,1,70,1,70,3,70,573,8,70,1,71,
        1,71,1,72,1,72,1,72,1,72,1,72,1,72,3,72,583,8,72,1,72,1,72,1,72,
        1,72,1,72,1,72,1,72,3,72,592,8,72,1,73,1,73,1,73,1,73,1,73,3,73,
        599,8,73,1,74,3,74,602,8,74,1,74,1,74,3,74,606,8,74,1,75,1,75,1,
        75,1,76,1,76,1,77,1,77,1,78,1,78,1,78,1,78,1,79,1,79,1,80,1,80,3,
        80,623,8,80,1,80,1,80,1,80,1,81,1,81,1,81,1,81,1,81,1,81,3,81,634,
        8,81,1,82,1,82,1,82,1,82,1,82,3,82,641,8,82,1,83,1,83,1,84,1,84,
        1,84,1,84,1,84,3,84,650,8,84,1,85,1,85,1,85,1,86,1,86,1,86,1,87,
        1,87,1,87,1,88,1,88,1,88,1,88,1,89,1,89,1,89,1,90,1,90,1,90,1,91,
        1,91,1,91,3,91,674,8,91,1,92,1,92,1,93,1,93,1,93,1,94,1,94,1,95,
        1,95,1,96,1,96,3,96,687,8,96,1,96,1,96,1,97,1,97,1,97,1,97,1,97,
        3,97,696,8,97,1,98,1,98,1,98,1,98,1,99,1,99,3,99,704,8,99,1,99,1,
        99,1,100,1,100,1,100,1,100,1,100,3,100,713,8,100,1,101,1,101,1,101,
        3,101,718,8,101,1,101,0,0,102,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
        70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,
        110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,
        142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,
        174,176,178,180,182,184,186,188,190,192,194,196,198,200,202,0,5,
        2,0,6,6,59,59,2,0,60,61,65,66,2,0,55,56,64,64,1,0,62,63,4,0,16,16,
        28,28,35,48,67,67,699,0,206,1,0,0,0,2,208,1,0,0,0,4,211,1,0,0,0,
        6,219,1,0,0,0,8,221,1,0,0,0,10,226,1,0,0,0,12,236,1,0,0,0,14,238,
        1,0,0,0,16,247,1,0,0,0,18,249,1,0,0,0,20,257,1,0,0,0,22,265,1,0,
        0,0,24,271,1,0,0,0,26,275,1,0,0,0,28,283,1,0,0,0,30,291,1,0,0,0,
        32,299,1,0,0,0,34,307,1,0,0,0,36,315,1,0,0,0,38,330,1,0,0,0,40,355,
        1,0,0,0,42,363,1,0,0,0,44,365,1,0,0,0,46,367,1,0,0,0,48,371,1,0,
        0,0,50,373,1,0,0,0,52,375,1,0,0,0,54,378,1,0,0,0,56,382,1,0,0,0,
        58,386,1,0,0,0,60,393,1,0,0,0,62,395,1,0,0,0,64,406,1,0,0,0,66,413,
        1,0,0,0,68,415,1,0,0,0,70,426,1,0,0,0,72,428,1,0,0,0,74,432,1,0,
        0,0,76,434,1,0,0,0,78,438,1,0,0,0,80,440,1,0,0,0,82,444,1,0,0,0,
        84,449,1,0,0,0,86,451,1,0,0,0,88,455,1,0,0,0,90,465,1,0,0,0,92,469,
        1,0,0,0,94,471,1,0,0,0,96,482,1,0,0,0,98,489,1,0,0,0,100,496,1,0,
        0,0,102,498,1,0,0,0,104,502,1,0,0,0,106,504,1,0,0,0,108,506,1,0,
        0,0,110,508,1,0,0,0,112,516,1,0,0,0,114,518,1,0,0,0,116,521,1,0,
        0,0,118,524,1,0,0,0,120,526,1,0,0,0,122,536,1,0,0,0,124,538,1,0,
        0,0,126,542,1,0,0,0,128,544,1,0,0,0,130,551,1,0,0,0,132,553,1,0,
        0,0,134,555,1,0,0,0,136,560,1,0,0,0,138,564,1,0,0,0,140,572,1,0,
        0,0,142,574,1,0,0,0,144,591,1,0,0,0,146,598,1,0,0,0,148,601,1,0,
        0,0,150,607,1,0,0,0,152,610,1,0,0,0,154,612,1,0,0,0,156,614,1,0,
        0,0,158,618,1,0,0,0,160,620,1,0,0,0,162,633,1,0,0,0,164,640,1,0,
        0,0,166,642,1,0,0,0,168,649,1,0,0,0,170,651,1,0,0,0,172,654,1,0,
        0,0,174,657,1,0,0,0,176,660,1,0,0,0,178,664,1,0,0,0,180,667,1,0,
        0,0,182,670,1,0,0,0,184,675,1,0,0,0,186,677,1,0,0,0,188,680,1,0,
        0,0,190,682,1,0,0,0,192,684,1,0,0,0,194,695,1,0,0,0,196,697,1,0,
        0,0,198,701,1,0,0,0,200,712,1,0,0,0,202,717,1,0,0,0,204,207,3,2,
        1,0,205,207,3,14,7,0,206,204,1,0,0,0,206,205,1,0,0,0,207,1,1,0,0,
        0,208,209,3,4,2,0,209,3,1,0,0,0,210,212,3,190,95,0,211,210,1,0,0,
        0,211,212,1,0,0,0,212,213,1,0,0,0,213,214,5,19,0,0,214,215,3,6,3,
        0,215,217,5,18,0,0,216,218,3,8,4,0,217,216,1,0,0,0,217,218,1,0,0,
        0,218,5,1,0,0,0,219,220,5,69,0,0,220,7,1,0,0,0,221,223,3,10,5,0,
        222,224,3,8,4,0,223,222,1,0,0,0,223,224,1,0,0,0,224,9,1,0,0,0,225,
        227,3,190,95,0,226,225,1,0,0,0,226,227,1,0,0,0,227,229,1,0,0,0,228,
        230,5,20,0,0,229,228,1,0,0,0,229,230,1,0,0,0,230,231,1,0,0,0,231,
        232,3,12,6,0,232,233,5,6,0,0,233,234,3,16,8,0,234,235,5,18,0,0,235,
        11,1,0,0,0,236,237,5,69,0,0,237,13,1,0,0,0,238,239,3,16,8,0,239,
        15,1,0,0,0,240,248,3,116,58,0,241,248,3,94,47,0,242,248,3,120,60,
        0,243,248,3,128,64,0,244,248,3,180,90,0,245,248,3,182,91,0,246,248,
        3,18,9,0,247,240,1,0,0,0,247,241,1,0,0,0,247,242,1,0,0,0,247,243,
        1,0,0,0,247,244,1,0,0,0,247,245,1,0,0,0,247,246,1,0,0,0,248,17,1,
        0,0,0,249,254,3,20,10,0,250,251,5,22,0,0,251,253,3,20,10,0,252,250,
        1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,255,1,0,0,0,255,19,1,
        0,0,0,256,254,1,0,0,0,257,262,3,22,11,0,258,259,5,21,0,0,259,261,
        3,22,11,0,260,258,1,0,0,0,261,264,1,0,0,0,262,260,1,0,0,0,262,263,
        1,0,0,0,263,21,1,0,0,0,264,262,1,0,0,0,265,268,3,26,13,0,266,267,
        5,58,0,0,267,269,3,24,12,0,268,266,1,0,0,0,268,269,1,0,0,0,269,23,
        1,0,0,0,270,272,5,17,0,0,271,270,1,0,0,0,271,272,1,0,0,0,272,273,
        1,0,0,0,273,274,3,142,71,0,274,25,1,0,0,0,275,280,3,28,14,0,276,
        277,5,50,0,0,277,279,3,24,12,0,278,276,1,0,0,0,279,282,1,0,0,0,280,
        278,1,0,0,0,280,281,1,0,0,0,281,27,1,0,0,0,282,280,1,0,0,0,283,288,
        3,30,15,0,284,285,7,0,0,0,285,287,3,30,15,0,286,284,1,0,0,0,287,
        290,1,0,0,0,288,286,1,0,0,0,288,289,1,0,0,0,289,29,1,0,0,0,290,288,
        1,0,0,0,291,296,3,32,16,0,292,293,7,1,0,0,293,295,3,32,16,0,294,
        292,1,0,0,0,295,298,1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,
        31,1,0,0,0,298,296,1,0,0,0,299,304,3,34,17,0,300,301,7,2,0,0,301,
        303,3,34,17,0,302,300,1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,
        305,1,0,0,0,305,33,1,0,0,0,306,304,1,0,0,0,307,312,3,36,18,0,308,
        309,7,3,0,0,309,311,3,36,18,0,310,308,1,0,0,0,311,314,1,0,0,0,312,
        310,1,0,0,0,312,313,1,0,0,0,313,35,1,0,0,0,314,312,1,0,0,0,315,320,
        3,38,19,0,316,317,5,57,0,0,317,319,3,38,19,0,318,316,1,0,0,0,319,
        322,1,0,0,0,320,318,1,0,0,0,320,321,1,0,0,0,321,37,1,0,0,0,322,320,
        1,0,0,0,323,324,5,55,0,0,324,331,3,38,19,0,325,326,5,56,0,0,326,
        331,3,38,19,0,327,328,5,54,0,0,328,331,3,38,19,0,329,331,3,136,68,
        0,330,323,1,0,0,0,330,325,1,0,0,0,330,327,1,0,0,0,330,329,1,0,0,
        0,331,39,1,0,0,0,332,349,3,42,21,0,333,348,3,78,39,0,334,348,3,86,
        43,0,335,348,3,88,44,0,336,337,5,10,0,0,337,338,3,76,38,0,338,340,
        5,11,0,0,339,341,5,14,0,0,340,339,1,0,0,0,340,341,1,0,0,0,341,348,
        1,0,0,0,342,344,5,12,0,0,343,345,3,60,30,0,344,343,1,0,0,0,344,345,
        1,0,0,0,345,346,1,0,0,0,346,348,5,13,0,0,347,333,1,0,0,0,347,334,
        1,0,0,0,347,335,1,0,0,0,347,336,1,0,0,0,347,342,1,0,0,0,348,351,
        1,0,0,0,349,347,1,0,0,0,349,350,1,0,0,0,350,356,1,0,0,0,351,349,
        1,0,0,0,352,356,3,84,42,0,353,356,3,92,46,0,354,356,3,58,29,0,355,
        332,1,0,0,0,355,352,1,0,0,0,355,353,1,0,0,0,355,354,1,0,0,0,356,
        41,1,0,0,0,357,364,3,44,22,0,358,364,3,62,31,0,359,364,3,68,34,0,
        360,364,3,46,23,0,361,364,3,54,27,0,362,364,3,56,28,0,363,357,1,
        0,0,0,363,358,1,0,0,0,363,359,1,0,0,0,363,360,1,0,0,0,363,361,1,
        0,0,0,363,362,1,0,0,0,364,43,1,0,0,0,365,366,5,67,0,0,366,45,1,0,
        0,0,367,368,3,48,24,0,368,47,1,0,0,0,369,372,3,50,25,0,370,372,3,
        52,26,0,371,369,1,0,0,0,371,370,1,0,0,0,372,49,1,0,0,0,373,374,5,
        69,0,0,374,51,1,0,0,0,375,376,5,49,0,0,376,377,5,69,0,0,377,53,1,
        0,0,0,378,379,5,69,0,0,379,380,5,53,0,0,380,381,5,69,0,0,381,55,
        1,0,0,0,382,383,5,12,0,0,383,384,3,16,8,0,384,385,5,13,0,0,385,57,
        1,0,0,0,386,387,5,27,0,0,387,59,1,0,0,0,388,394,3,16,8,0,389,390,
        3,16,8,0,390,391,5,7,0,0,391,392,3,60,30,0,392,394,1,0,0,0,393,388,
        1,0,0,0,393,389,1,0,0,0,394,61,1,0,0,0,395,397,5,10,0,0,396,398,
        3,64,32,0,397,396,1,0,0,0,397,398,1,0,0,0,398,399,1,0,0,0,399,400,
        5,11,0,0,400,63,1,0,0,0,401,407,3,66,33,0,402,403,3,66,33,0,403,
        404,5,7,0,0,404,405,3,64,32,0,405,407,1,0,0,0,406,401,1,0,0,0,406,
        402,1,0,0,0,407,65,1,0,0,0,408,414,3,16,8,0,409,410,3,16,8,0,410,
        411,5,52,0,0,411,412,3,16,8,0,412,414,1,0,0,0,413,408,1,0,0,0,413,
        409,1,0,0,0,414,67,1,0,0,0,415,417,5,8,0,0,416,418,3,70,35,0,417,
        416,1,0,0,0,417,418,1,0,0,0,418,419,1,0,0,0,419,420,5,9,0,0,420,
        69,1,0,0,0,421,427,3,72,36,0,422,423,3,72,36,0,423,424,5,7,0,0,424,
        425,3,70,35,0,425,427,1,0,0,0,426,421,1,0,0,0,426,422,1,0,0,0,427,
        71,1,0,0,0,428,429,3,74,37,0,429,430,5,6,0,0,430,431,3,16,8,0,431,
        73,1,0,0,0,432,433,5,69,0,0,433,75,1,0,0,0,434,435,3,16,8,0,435,
        77,1,0,0,0,436,439,3,80,40,0,437,439,3,82,41,0,438,436,1,0,0,0,438,
        437,1,0,0,0,439,79,1,0,0,0,440,441,5,8,0,0,441,442,3,74,37,0,442,
        443,5,9,0,0,443,81,1,0,0,0,444,445,5,8,0,0,445,446,3,74,37,0,446,
        447,5,9,0,0,447,448,5,14,0,0,448,83,1,0,0,0,449,450,3,78,39,0,450,
        85,1,0,0,0,451,452,5,8,0,0,452,453,3,90,45,0,453,454,5,9,0,0,454,
        87,1,0,0,0,455,456,5,8,0,0,456,457,3,90,45,0,457,458,5,9,0,0,458,
        459,5,14,0,0,459,89,1,0,0,0,460,466,3,80,40,0,461,462,3,80,40,0,
        462,463,5,7,0,0,463,464,3,90,45,0,464,466,1,0,0,0,465,460,1,0,0,
        0,465,461,1,0,0,0,466,91,1,0,0,0,467,470,3,86,43,0,468,470,3,88,
        44,0,469,467,1,0,0,0,469,468,1,0,0,0,470,93,1,0,0,0,471,473,5,12,
        0,0,472,474,3,98,49,0,473,472,1,0,0,0,473,474,1,0,0,0,474,475,1,
        0,0,0,475,477,5,13,0,0,476,478,3,108,54,0,477,476,1,0,0,0,477,478,
        1,0,0,0,478,479,1,0,0,0,479,480,5,51,0,0,480,481,3,96,48,0,481,95,
        1,0,0,0,482,483,3,16,8,0,483,97,1,0,0,0,484,490,3,100,50,0,485,486,
        3,100,50,0,486,487,5,7,0,0,487,488,3,112,56,0,488,490,1,0,0,0,489,
        484,1,0,0,0,489,485,1,0,0,0,490,99,1,0,0,0,491,497,3,102,51,0,492,
        493,3,102,51,0,493,494,5,7,0,0,494,495,3,100,50,0,495,497,1,0,0,
        0,496,491,1,0,0,0,496,492,1,0,0,0,497,101,1,0,0,0,498,500,3,104,
        52,0,499,501,3,106,53,0,500,499,1,0,0,0,500,501,1,0,0,0,501,103,
        1,0,0,0,502,503,5,69,0,0,503,105,1,0,0,0,504,505,3,110,55,0,505,
        107,1,0,0,0,506,507,3,110,55,0,507,109,1,0,0,0,508,509,5,50,0,0,
        509,510,3,24,12,0,510,111,1,0,0,0,511,517,3,114,57,0,512,513,3,114,
        57,0,513,514,5,7,0,0,514,515,3,112,56,0,515,517,1,0,0,0,516,511,
        1,0,0,0,516,512,1,0,0,0,517,113,1,0,0,0,518,519,5,15,0,0,519,520,
        3,102,51,0,520,115,1,0,0,0,521,522,5,29,0,0,522,523,3,118,59,0,523,
        117,1,0,0,0,524,525,3,96,48,0,525,119,1,0,0,0,526,527,5,30,0,0,527,
        528,3,122,61,0,528,529,5,31,0,0,529,530,3,16,8,0,530,121,1,0,0,0,
        531,537,3,124,62,0,532,533,3,124,62,0,533,534,5,7,0,0,534,535,3,
        122,61,0,535,537,1,0,0,0,536,531,1,0,0,0,536,532,1,0,0,0,537,123,
        1,0,0,0,538,539,3,126,63,0,539,540,5,6,0,0,540,541,3,16,8,0,541,
        125,1,0,0,0,542,543,5,69,0,0,543,127,1,0,0,0,544,545,5,32,0,0,545,
        546,3,130,65,0,546,547,5,33,0,0,547,548,3,132,66,0,548,549,5,34,
        0,0,549,550,3,134,67,0,550,129,1,0,0,0,551,552,3,16,8,0,552,131,
        1,0,0,0,553,554,3,16,8,0,554,133,1,0,0,0,555,556,3,16,8,0,556,135,
        1,0,0,0,557,561,3,40,20,0,558,559,5,28,0,0,559,561,3,140,70,0,560,
        557,1,0,0,0,560,558,1,0,0,0,561,137,1,0,0,0,562,565,3,56,28,0,563,
        565,3,140,70,0,564,562,1,0,0,0,564,563,1,0,0,0,565,139,1,0,0,0,566,
        573,3,142,71,0,567,573,3,144,72,0,568,573,3,156,78,0,569,573,3,160,
        80,0,570,573,3,174,87,0,571,573,3,178,89,0,572,566,1,0,0,0,572,567,
        1,0,0,0,572,568,1,0,0,0,572,569,1,0,0,0,572,570,1,0,0,0,572,571,
        1,0,0,0,573,141,1,0,0,0,574,575,7,4,0,0,575,143,1,0,0,0,576,577,
        5,8,0,0,577,578,3,154,77,0,578,579,5,9,0,0,579,592,1,0,0,0,580,582,
        5,8,0,0,581,583,3,146,73,0,582,581,1,0,0,0,582,583,1,0,0,0,583,584,
        1,0,0,0,584,592,5,9,0,0,585,586,5,8,0,0,586,587,3,146,73,0,587,588,
        5,7,0,0,588,589,3,154,77,0,589,590,5,9,0,0,590,592,1,0,0,0,591,576,
        1,0,0,0,591,580,1,0,0,0,591,585,1,0,0,0,592,145,1,0,0,0,593,599,
        3,148,74,0,594,595,3,148,74,0,595,596,5,7,0,0,596,597,3,146,73,0,
        597,599,1,0,0,0,598,593,1,0,0,0,598,594,1,0,0,0,599,147,1,0,0,0,
        600,602,5,15,0,0,601,600,1,0,0,0,601,602,1,0,0,0,602,603,1,0,0,0,
        603,605,3,74,37,0,604,606,3,150,75,0,605,604,1,0,0,0,605,606,1,0,
        0,0,606,149,1,0,0,0,607,608,5,6,0,0,608,609,3,152,76,0,609,151,1,
        0,0,0,610,611,3,138,69,0,611,153,1,0,0,0,612,613,5,27,0,0,613,155,
        1,0,0,0,614,615,5,10,0,0,615,616,3,158,79,0,616,617,5,11,0,0,617,
        157,1,0,0,0,618,619,3,138,69,0,619,159,1,0,0,0,620,622,5,26,0,0,
        621,623,3,162,81,0,622,621,1,0,0,0,622,623,1,0,0,0,623,624,1,0,0,
        0,624,625,5,13,0,0,625,626,3,108,54,0,626,161,1,0,0,0,627,634,3,
        164,82,0,628,629,3,164,82,0,629,630,5,7,0,0,630,631,3,168,84,0,631,
        634,1,0,0,0,632,634,3,168,84,0,633,627,1,0,0,0,633,628,1,0,0,0,633,
        632,1,0,0,0,634,163,1,0,0,0,635,641,3,166,83,0,636,637,3,166,83,
        0,637,638,5,7,0,0,638,639,3,164,82,0,639,641,1,0,0,0,640,635,1,0,
        0,0,640,636,1,0,0,0,641,165,1,0,0,0,642,643,3,172,86,0,643,167,1,
        0,0,0,644,650,3,170,85,0,645,646,3,170,85,0,646,647,5,7,0,0,647,
        648,3,168,84,0,648,650,1,0,0,0,649,644,1,0,0,0,649,645,1,0,0,0,650,
        169,1,0,0,0,651,652,5,15,0,0,652,653,3,172,86,0,653,171,1,0,0,0,
        654,655,3,104,52,0,655,656,3,106,53,0,656,173,1,0,0,0,657,658,5,
        16,0,0,658,659,3,176,88,0,659,175,1,0,0,0,660,661,5,8,0,0,661,662,
        3,146,73,0,662,663,5,9,0,0,663,177,1,0,0,0,664,665,5,17,0,0,665,
        666,3,138,69,0,666,179,1,0,0,0,667,668,5,25,0,0,668,669,3,16,8,0,
        669,181,1,0,0,0,670,671,5,24,0,0,671,673,3,184,92,0,672,674,3,186,
        93,0,673,672,1,0,0,0,673,674,1,0,0,0,674,183,1,0,0,0,675,676,3,16,
        8,0,676,185,1,0,0,0,677,678,5,23,0,0,678,679,3,188,94,0,679,187,
        1,0,0,0,680,681,3,16,8,0,681,189,1,0,0,0,682,683,3,192,96,0,683,
        191,1,0,0,0,684,686,5,8,0,0,685,687,3,194,97,0,686,685,1,0,0,0,686,
        687,1,0,0,0,687,688,1,0,0,0,688,689,5,9,0,0,689,193,1,0,0,0,690,
        696,3,196,98,0,691,692,3,196,98,0,692,693,5,7,0,0,693,694,3,194,
        97,0,694,696,1,0,0,0,695,690,1,0,0,0,695,691,1,0,0,0,696,195,1,0,
        0,0,697,698,3,74,37,0,698,699,5,6,0,0,699,700,3,202,101,0,700,197,
        1,0,0,0,701,703,5,10,0,0,702,704,3,200,100,0,703,702,1,0,0,0,703,
        704,1,0,0,0,704,705,1,0,0,0,705,706,5,11,0,0,706,199,1,0,0,0,707,
        713,3,202,101,0,708,709,3,202,101,0,709,710,5,7,0,0,710,711,3,200,
        100,0,711,713,1,0,0,0,712,707,1,0,0,0,712,708,1,0,0,0,713,201,1,
        0,0,0,714,718,3,192,96,0,715,718,3,198,99,0,716,718,5,67,0,0,717,
        714,1,0,0,0,717,715,1,0,0,0,717,716,1,0,0,0,718,203,1,0,0,0,59,206,
        211,217,223,226,229,247,254,262,268,271,280,288,296,304,312,320,
        330,340,344,347,349,355,363,371,393,397,406,413,417,426,438,465,
        469,473,477,489,496,500,516,536,560,564,572,582,591,598,601,605,
        622,633,640,649,673,686,695,703,712,717
    ]

class PowerQueryParser ( Parser ):

    grammarFileName = "PowerQueryParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'='", "','", "'['", "']'", 
                     "'{'", "'}'", "'('", "')'", "'?'", "'optional'", "'table'", 
                     "'nullable'", "';'", "'section'", "'shared'", "'and'", 
                     "'or'", "'otherwise'", "'try'", "'error'", "'function ('", 
                     "'...'", "'type'", "'each'", "'let'", "'in'", "'if'", 
                     "'then'", "'else'", "'text'", "'record'", "'number'", 
                     "'none'", "'logical'", "'list'", "'fuction'", "'duration'", 
                     "'datetimezone'", "'any'", "'anynonnull'", "'binary'", 
                     "'date'", "'datetime'", "'@'", "'as'", "'=>'", "'..'", 
                     "'!'", "'not'", "'+'", "'-'", "'meta'", "'is'", "'<>'", 
                     "'>'", "'<'", "'/'", "'*'", "'&'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "NEW_LINE_CHAR", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "CHARACHTER_ESCAPE_SEQUENCE", "EQUALS", 
                      "COMMA", "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", 
                      "CLOSE_BRACE", "OPEN_PAREN", "CLOSE_PAREN", "OPTIONAL", 
                      "OPTIONAL_TEXT", "TABLE", "NULLABLE", "SEMICOLON", 
                      "SECTION", "SHARED", "AND", "OR", "OTHERWISE", "TRY", 
                      "ERROR", "FUNCTION_START", "ELLIPSES", "TYPE", "EACH", 
                      "LET", "IN", "IF", "THEN", "ELSE", "TEXT", "RECORD", 
                      "NUMBER", "NONE", "LOGICAL", "LIST", "FUNCTION", "DURATION", 
                      "DATETIMEZONE", "ANY", "ANYNONNULL", "BINARY", "DATE", 
                      "DATETIME", "AT", "AS", "ARROW", "DOTDOT", "BANG", 
                      "NOT", "PLUS", "MINUS", "META", "IS", "NEQ", "GE", 
                      "LE", "SLASH", "STAR", "AMP", "LEQ", "GEQ", "LITERAL", 
                      "TEXT_LITERAL", "IDENTIFIER", "REGULAR_IDENTIFIER", 
                      "AVAILABLE_IDENTIFIER", "KEYWORD_OR_IDENTIFIER" ]

    RULE_document = 0
    RULE_section_document = 1
    RULE_section = 2
    RULE_section_name = 3
    RULE_section_members = 4
    RULE_section_member = 5
    RULE_section_member_name = 6
    RULE_expression_document = 7
    RULE_expression = 8
    RULE_logical_or_expression = 9
    RULE_logical_and_expression = 10
    RULE_is_expression = 11
    RULE_nullable_primitive_type = 12
    RULE_as_expression = 13
    RULE_equality_expression = 14
    RULE_relational_expression = 15
    RULE_additive_expression = 16
    RULE_multiplicative_expression = 17
    RULE_metadata_expression = 18
    RULE_unary_expression = 19
    RULE_primary_expression = 20
    RULE_atom = 21
    RULE_literal_expression = 22
    RULE_identifier_expression = 23
    RULE_identifier_reference = 24
    RULE_exclusive_identifier_reference = 25
    RULE_inclusive_identifier_reference = 26
    RULE_section_access_expression = 27
    RULE_parenthesized_expression = 28
    RULE_not_implemented_expression = 29
    RULE_argument_list = 30
    RULE_list_expression = 31
    RULE_item_list = 32
    RULE_item = 33
    RULE_record_expression = 34
    RULE_field_list = 35
    RULE_field = 36
    RULE_field_name = 37
    RULE_item_selector = 38
    RULE_field_selector = 39
    RULE_required_field_selector = 40
    RULE_optional_field_selector = 41
    RULE_implicit_target_field_selection = 42
    RULE_required_projection = 43
    RULE_optional_projection = 44
    RULE_required_selector_list = 45
    RULE_implicit_target_projection = 46
    RULE_function_expression = 47
    RULE_function_body = 48
    RULE_parameter_list = 49
    RULE_fixed_parameter_list = 50
    RULE_parameter = 51
    RULE_parameter_name = 52
    RULE_parameter_type = 53
    RULE_return_type = 54
    RULE_assertion = 55
    RULE_optional_parameter_list = 56
    RULE_optional_parameter = 57
    RULE_each_expression = 58
    RULE_each_expression_body = 59
    RULE_let_expression = 60
    RULE_variable_list = 61
    RULE_variable = 62
    RULE_variable_name = 63
    RULE_if_expression = 64
    RULE_if_condition = 65
    RULE_true_expression = 66
    RULE_false_expression = 67
    RULE_type_expression = 68
    RULE_type_expr = 69
    RULE_primary_type = 70
    RULE_primitive_type = 71
    RULE_record_type = 72
    RULE_field_specification_list = 73
    RULE_field_specification = 74
    RULE_field_type_specification = 75
    RULE_field_type = 76
    RULE_open_record_marker = 77
    RULE_list_type = 78
    RULE_item_type = 79
    RULE_function_type = 80
    RULE_parameter_specification_list = 81
    RULE_required_parameter_specification_list = 82
    RULE_required_parameter_specification = 83
    RULE_optional_parameter_specification_list = 84
    RULE_optional_parameter_specification = 85
    RULE_parameter_specification = 86
    RULE_table_type = 87
    RULE_row_type = 88
    RULE_nullable_type = 89
    RULE_error_raising_expression = 90
    RULE_error_handling_expression = 91
    RULE_protected_expression = 92
    RULE_otherwise_clause = 93
    RULE_default_expression = 94
    RULE_literal_attribs = 95
    RULE_record_literal = 96
    RULE_literal_field_list = 97
    RULE_literal_field = 98
    RULE_list_literal = 99
    RULE_literal_item_list = 100
    RULE_any_literal = 101

    ruleNames =  [ "document", "section_document", "section", "section_name", 
                   "section_members", "section_member", "section_member_name", 
                   "expression_document", "expression", "logical_or_expression", 
                   "logical_and_expression", "is_expression", "nullable_primitive_type", 
                   "as_expression", "equality_expression", "relational_expression", 
                   "additive_expression", "multiplicative_expression", "metadata_expression", 
                   "unary_expression", "primary_expression", "atom", "literal_expression", 
                   "identifier_expression", "identifier_reference", "exclusive_identifier_reference", 
                   "inclusive_identifier_reference", "section_access_expression", 
                   "parenthesized_expression", "not_implemented_expression", 
                   "argument_list", "list_expression", "item_list", "item", 
                   "record_expression", "field_list", "field", "field_name", 
                   "item_selector", "field_selector", "required_field_selector", 
                   "optional_field_selector", "implicit_target_field_selection", 
                   "required_projection", "optional_projection", "required_selector_list", 
                   "implicit_target_projection", "function_expression", 
                   "function_body", "parameter_list", "fixed_parameter_list", 
                   "parameter", "parameter_name", "parameter_type", "return_type", 
                   "assertion", "optional_parameter_list", "optional_parameter", 
                   "each_expression", "each_expression_body", "let_expression", 
                   "variable_list", "variable", "variable_name", "if_expression", 
                   "if_condition", "true_expression", "false_expression", 
                   "type_expression", "type_expr", "primary_type", "primitive_type", 
                   "record_type", "field_specification_list", "field_specification", 
                   "field_type_specification", "field_type", "open_record_marker", 
                   "list_type", "item_type", "function_type", "parameter_specification_list", 
                   "required_parameter_specification_list", "required_parameter_specification", 
                   "optional_parameter_specification_list", "optional_parameter_specification", 
                   "parameter_specification", "table_type", "row_type", 
                   "nullable_type", "error_raising_expression", "error_handling_expression", 
                   "protected_expression", "otherwise_clause", "default_expression", 
                   "literal_attribs", "record_literal", "literal_field_list", 
                   "literal_field", "list_literal", "literal_item_list", 
                   "any_literal" ]

    EOF = Token.EOF
    WHITESPACE=1
    NEW_LINE_CHAR=2
    LINE_COMMENT=3
    BLOCK_COMMENT=4
    CHARACHTER_ESCAPE_SEQUENCE=5
    EQUALS=6
    COMMA=7
    OPEN_BRACKET=8
    CLOSE_BRACKET=9
    OPEN_BRACE=10
    CLOSE_BRACE=11
    OPEN_PAREN=12
    CLOSE_PAREN=13
    OPTIONAL=14
    OPTIONAL_TEXT=15
    TABLE=16
    NULLABLE=17
    SEMICOLON=18
    SECTION=19
    SHARED=20
    AND=21
    OR=22
    OTHERWISE=23
    TRY=24
    ERROR=25
    FUNCTION_START=26
    ELLIPSES=27
    TYPE=28
    EACH=29
    LET=30
    IN=31
    IF=32
    THEN=33
    ELSE=34
    TEXT=35
    RECORD=36
    NUMBER=37
    NONE=38
    LOGICAL=39
    LIST=40
    FUNCTION=41
    DURATION=42
    DATETIMEZONE=43
    ANY=44
    ANYNONNULL=45
    BINARY=46
    DATE=47
    DATETIME=48
    AT=49
    AS=50
    ARROW=51
    DOTDOT=52
    BANG=53
    NOT=54
    PLUS=55
    MINUS=56
    META=57
    IS=58
    NEQ=59
    GE=60
    LE=61
    SLASH=62
    STAR=63
    AMP=64
    LEQ=65
    GEQ=66
    LITERAL=67
    TEXT_LITERAL=68
    IDENTIFIER=69
    REGULAR_IDENTIFIER=70
    AVAILABLE_IDENTIFIER=71
    KEYWORD_OR_IDENTIFIER=72

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def section_document(self):
            return self.getTypedRuleContext(PowerQueryParser.Section_documentContext,0)


        def expression_document(self):
            return self.getTypedRuleContext(PowerQueryParser.Expression_documentContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)




    def document(self):

        localctx = PowerQueryParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.section_document()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.expression_document()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_documentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def section(self):
            return self.getTypedRuleContext(PowerQueryParser.SectionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_section_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_document" ):
                listener.enterSection_document(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_document" ):
                listener.exitSection_document(self)




    def section_document(self):

        localctx = PowerQueryParser.Section_documentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_section_document)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.section()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SECTION(self):
            return self.getToken(PowerQueryParser.SECTION, 0)

        def section_name(self):
            return self.getTypedRuleContext(PowerQueryParser.Section_nameContext,0)


        def SEMICOLON(self):
            return self.getToken(PowerQueryParser.SEMICOLON, 0)

        def literal_attribs(self):
            return self.getTypedRuleContext(PowerQueryParser.Literal_attribsContext,0)


        def section_members(self):
            return self.getTypedRuleContext(PowerQueryParser.Section_membersContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)




    def section(self):

        localctx = PowerQueryParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 210
                self.literal_attribs()


            self.state = 213
            self.match(PowerQueryParser.SECTION)
            self.state = 214
            self.section_name()
            self.state = 215
            self.match(PowerQueryParser.SEMICOLON)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 2305843009213698049) != 0):
                self.state = 216
                self.section_members()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PowerQueryParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_section_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_name" ):
                listener.enterSection_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_name" ):
                listener.exitSection_name(self)




    def section_name(self):

        localctx = PowerQueryParser.Section_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_section_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(PowerQueryParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_membersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def section_member(self):
            return self.getTypedRuleContext(PowerQueryParser.Section_memberContext,0)


        def section_members(self):
            return self.getTypedRuleContext(PowerQueryParser.Section_membersContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_section_members

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_members" ):
                listener.enterSection_members(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_members" ):
                listener.exitSection_members(self)




    def section_members(self):

        localctx = PowerQueryParser.Section_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_section_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.section_member()
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 2305843009213698049) != 0):
                self.state = 222
                self.section_members()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def section_member_name(self):
            return self.getTypedRuleContext(PowerQueryParser.Section_member_nameContext,0)


        def EQUALS(self):
            return self.getToken(PowerQueryParser.EQUALS, 0)

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(PowerQueryParser.SEMICOLON, 0)

        def literal_attribs(self):
            return self.getTypedRuleContext(PowerQueryParser.Literal_attribsContext,0)


        def SHARED(self):
            return self.getToken(PowerQueryParser.SHARED, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_section_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_member" ):
                listener.enterSection_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_member" ):
                listener.exitSection_member(self)




    def section_member(self):

        localctx = PowerQueryParser.Section_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_section_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 225
                self.literal_attribs()


            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 228
                self.match(PowerQueryParser.SHARED)


            self.state = 231
            self.section_member_name()
            self.state = 232
            self.match(PowerQueryParser.EQUALS)
            self.state = 233
            self.expression()
            self.state = 234
            self.match(PowerQueryParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_member_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PowerQueryParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_section_member_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_member_name" ):
                listener.enterSection_member_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_member_name" ):
                listener.exitSection_member_name(self)




    def section_member_name(self):

        localctx = PowerQueryParser.Section_member_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_section_member_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(PowerQueryParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_documentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_expression_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_document" ):
                listener.enterExpression_document(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_document" ):
                listener.exitExpression_document(self)




    def expression_document(self):

        localctx = PowerQueryParser.Expression_documentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression_document)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def each_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Each_expressionContext,0)


        def function_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Function_expressionContext,0)


        def let_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Let_expressionContext,0)


        def if_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.If_expressionContext,0)


        def error_raising_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Error_raising_expressionContext,0)


        def error_handling_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Error_handling_expressionContext,0)


        def logical_or_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Logical_or_expressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = PowerQueryParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.each_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.function_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.let_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.if_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                self.error_raising_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 245
                self.error_handling_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 246
                self.logical_or_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_or_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_and_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Logical_and_expressionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Logical_and_expressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.OR)
            else:
                return self.getToken(PowerQueryParser.OR, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_logical_or_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_or_expression" ):
                listener.enterLogical_or_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_or_expression" ):
                listener.exitLogical_or_expression(self)




    def logical_or_expression(self):

        localctx = PowerQueryParser.Logical_or_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_logical_or_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.logical_and_expression()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 250
                self.match(PowerQueryParser.OR)
                self.state = 251
                self.logical_and_expression()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_and_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def is_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Is_expressionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Is_expressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.AND)
            else:
                return self.getToken(PowerQueryParser.AND, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_logical_and_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_and_expression" ):
                listener.enterLogical_and_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_and_expression" ):
                listener.exitLogical_and_expression(self)




    def logical_and_expression(self):

        localctx = PowerQueryParser.Logical_and_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_logical_and_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.is_expression()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 258
                self.match(PowerQueryParser.AND)
                self.state = 259
                self.is_expression()
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Is_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def as_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.As_expressionContext,0)


        def IS(self):
            return self.getToken(PowerQueryParser.IS, 0)

        def nullable_primitive_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Nullable_primitive_typeContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_is_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIs_expression" ):
                listener.enterIs_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIs_expression" ):
                listener.exitIs_expression(self)




    def is_expression(self):

        localctx = PowerQueryParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_is_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.as_expression()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 266
                self.match(PowerQueryParser.IS)
                self.state = 267
                self.nullable_primitive_type()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Primitive_typeContext,0)


        def NULLABLE(self):
            return self.getToken(PowerQueryParser.NULLABLE, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_nullable_primitive_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullable_primitive_type" ):
                listener.enterNullable_primitive_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullable_primitive_type" ):
                listener.exitNullable_primitive_type(self)




    def nullable_primitive_type(self):

        localctx = PowerQueryParser.Nullable_primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_nullable_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 270
                self.match(PowerQueryParser.NULLABLE)


            self.state = 273
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class As_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Equality_expressionContext,0)


        def AS(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.AS)
            else:
                return self.getToken(PowerQueryParser.AS, i)

        def nullable_primitive_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Nullable_primitive_typeContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Nullable_primitive_typeContext,i)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_as_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAs_expression" ):
                listener.enterAs_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAs_expression" ):
                listener.exitAs_expression(self)




    def as_expression(self):

        localctx = PowerQueryParser.As_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_as_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.equality_expression()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 276
                self.match(PowerQueryParser.AS)
                self.state = 277
                self.nullable_primitive_type()
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equality_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Relational_expressionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Relational_expressionContext,i)


        def EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.EQUALS)
            else:
                return self.getToken(PowerQueryParser.EQUALS, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.NEQ)
            else:
                return self.getToken(PowerQueryParser.NEQ, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_equality_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality_expression" ):
                listener.enterEquality_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality_expression" ):
                listener.exitEquality_expression(self)




    def equality_expression(self):

        localctx = PowerQueryParser.Equality_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_equality_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.relational_expression()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==59:
                self.state = 284
                _la = self._input.LA(1)
                if not(_la==6 or _la==59):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 285
                self.relational_expression()
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Additive_expressionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Additive_expressionContext,i)


        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.LE)
            else:
                return self.getToken(PowerQueryParser.LE, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.GE)
            else:
                return self.getToken(PowerQueryParser.GE, i)

        def LEQ(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.LEQ)
            else:
                return self.getToken(PowerQueryParser.LEQ, i)

        def GEQ(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.GEQ)
            else:
                return self.getToken(PowerQueryParser.GEQ, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_relational_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_expression" ):
                listener.enterRelational_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_expression" ):
                listener.exitRelational_expression(self)




    def relational_expression(self):

        localctx = PowerQueryParser.Relational_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relational_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.additive_expression()
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 60)) & ~0x3f) == 0 and ((1 << (_la - 60)) & 99) != 0):
                self.state = 292
                _la = self._input.LA(1)
                if not(((((_la - 60)) & ~0x3f) == 0 and ((1 << (_la - 60)) & 99) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 293
                self.additive_expression()
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Additive_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Multiplicative_expressionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Multiplicative_expressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.PLUS)
            else:
                return self.getToken(PowerQueryParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.MINUS)
            else:
                return self.getToken(PowerQueryParser.MINUS, i)

        def AMP(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.AMP)
            else:
                return self.getToken(PowerQueryParser.AMP, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_additive_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive_expression" ):
                listener.enterAdditive_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive_expression" ):
                listener.exitAdditive_expression(self)




    def additive_expression(self):

        localctx = PowerQueryParser.Additive_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_additive_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.multiplicative_expression()
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 55)) & ~0x3f) == 0 and ((1 << (_la - 55)) & 515) != 0):
                self.state = 300
                _la = self._input.LA(1)
                if not(((((_la - 55)) & ~0x3f) == 0 and ((1 << (_la - 55)) & 515) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 301
                self.multiplicative_expression()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplicative_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metadata_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Metadata_expressionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Metadata_expressionContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.STAR)
            else:
                return self.getToken(PowerQueryParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.SLASH)
            else:
                return self.getToken(PowerQueryParser.SLASH, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_multiplicative_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative_expression" ):
                listener.enterMultiplicative_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative_expression" ):
                listener.exitMultiplicative_expression(self)




    def multiplicative_expression(self):

        localctx = PowerQueryParser.Multiplicative_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_multiplicative_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.metadata_expression()
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62 or _la==63:
                self.state = 308
                _la = self._input.LA(1)
                if not(_la==62 or _la==63):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 309
                self.metadata_expression()
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Metadata_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Unary_expressionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Unary_expressionContext,i)


        def META(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.META)
            else:
                return self.getToken(PowerQueryParser.META, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_metadata_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetadata_expression" ):
                listener.enterMetadata_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetadata_expression" ):
                listener.exitMetadata_expression(self)




    def metadata_expression(self):

        localctx = PowerQueryParser.Metadata_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_metadata_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.unary_expression()
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 316
                self.match(PowerQueryParser.META)
                self.state = 317
                self.unary_expression()
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(PowerQueryParser.PLUS, 0)

        def unary_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Unary_expressionContext,0)


        def MINUS(self):
            return self.getToken(PowerQueryParser.MINUS, 0)

        def NOT(self):
            return self.getToken(PowerQueryParser.NOT, 0)

        def type_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Type_expressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_unary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expression" ):
                listener.enterUnary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expression" ):
                listener.exitUnary_expression(self)




    def unary_expression(self):

        localctx = PowerQueryParser.Unary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unary_expression)
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(PowerQueryParser.PLUS)
                self.state = 324
                self.unary_expression()
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(PowerQueryParser.MINUS)
                self.state = 326
                self.unary_expression()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.match(PowerQueryParser.NOT)
                self.state = 328
                self.unary_expression()
                pass
            elif token in [8, 10, 12, 27, 28, 49, 67, 69]:
                self.enterOuterAlt(localctx, 4)
                self.state = 329
                self.type_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(PowerQueryParser.AtomContext,0)


        def field_selector(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Field_selectorContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Field_selectorContext,i)


        def required_projection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Required_projectionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Required_projectionContext,i)


        def optional_projection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Optional_projectionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Optional_projectionContext,i)


        def OPEN_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.OPEN_BRACE)
            else:
                return self.getToken(PowerQueryParser.OPEN_BRACE, i)

        def item_selector(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Item_selectorContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Item_selectorContext,i)


        def CLOSE_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.CLOSE_BRACE)
            else:
                return self.getToken(PowerQueryParser.CLOSE_BRACE, i)

        def OPEN_PAREN(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.OPEN_PAREN)
            else:
                return self.getToken(PowerQueryParser.OPEN_PAREN, i)

        def CLOSE_PAREN(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.CLOSE_PAREN)
            else:
                return self.getToken(PowerQueryParser.CLOSE_PAREN, i)

        def OPTIONAL(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.OPTIONAL)
            else:
                return self.getToken(PowerQueryParser.OPTIONAL, i)

        def argument_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Argument_listContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Argument_listContext,i)


        def implicit_target_field_selection(self):
            return self.getTypedRuleContext(PowerQueryParser.Implicit_target_field_selectionContext,0)


        def implicit_target_projection(self):
            return self.getTypedRuleContext(PowerQueryParser.Implicit_target_projectionContext,0)


        def not_implemented_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Not_implemented_expressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_primary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression" ):
                listener.enterPrimary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression" ):
                listener.exitPrimary_expression(self)




    def primary_expression(self):

        localctx = PowerQueryParser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_primary_expression)
        self._la = 0 # Token type
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.atom()
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5376) != 0):
                    self.state = 347
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        self.state = 333
                        self.field_selector()
                        pass

                    elif la_ == 2:
                        self.state = 334
                        self.required_projection()
                        pass

                    elif la_ == 3:
                        self.state = 335
                        self.optional_projection()
                        pass

                    elif la_ == 4:
                        self.state = 336
                        self.match(PowerQueryParser.OPEN_BRACE)
                        self.state = 337
                        self.item_selector()
                        self.state = 338
                        self.match(PowerQueryParser.CLOSE_BRACE)
                        self.state = 340
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==14:
                            self.state = 339
                            self.match(PowerQueryParser.OPTIONAL)


                        pass

                    elif la_ == 5:
                        self.state = 342
                        self.match(PowerQueryParser.OPEN_PAREN)
                        self.state = 344
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 2882798541774454805) != 0):
                            self.state = 343
                            self.argument_list()


                        self.state = 346
                        self.match(PowerQueryParser.CLOSE_PAREN)
                        pass


                    self.state = 351
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.implicit_target_field_selection()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
                self.implicit_target_projection()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 354
                self.not_implemented_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Literal_expressionContext,0)


        def list_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.List_expressionContext,0)


        def record_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Record_expressionContext,0)


        def identifier_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Identifier_expressionContext,0)


        def section_access_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Section_access_expressionContext,0)


        def parenthesized_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Parenthesized_expressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = PowerQueryParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_atom)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.literal_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.list_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 359
                self.record_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 360
                self.identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 361
                self.section_access_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 362
                self.parenthesized_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL(self):
            return self.getToken(PowerQueryParser.LITERAL, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_literal_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_expression" ):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_expression" ):
                listener.exitLiteral_expression(self)




    def literal_expression(self):

        localctx = PowerQueryParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(PowerQueryParser.LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_reference(self):
            return self.getTypedRuleContext(PowerQueryParser.Identifier_referenceContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_identifier_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier_expression" ):
                listener.enterIdentifier_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier_expression" ):
                listener.exitIdentifier_expression(self)




    def identifier_expression(self):

        localctx = PowerQueryParser.Identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.identifier_reference()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exclusive_identifier_reference(self):
            return self.getTypedRuleContext(PowerQueryParser.Exclusive_identifier_referenceContext,0)


        def inclusive_identifier_reference(self):
            return self.getTypedRuleContext(PowerQueryParser.Inclusive_identifier_referenceContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_identifier_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier_reference" ):
                listener.enterIdentifier_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier_reference" ):
                listener.exitIdentifier_reference(self)




    def identifier_reference(self):

        localctx = PowerQueryParser.Identifier_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_identifier_reference)
        try:
            self.state = 371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [69]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.exclusive_identifier_reference()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.inclusive_identifier_reference()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exclusive_identifier_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PowerQueryParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_exclusive_identifier_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExclusive_identifier_reference" ):
                listener.enterExclusive_identifier_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExclusive_identifier_reference" ):
                listener.exitExclusive_identifier_reference(self)




    def exclusive_identifier_reference(self):

        localctx = PowerQueryParser.Exclusive_identifier_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exclusive_identifier_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(PowerQueryParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inclusive_identifier_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(PowerQueryParser.AT, 0)

        def IDENTIFIER(self):
            return self.getToken(PowerQueryParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_inclusive_identifier_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclusive_identifier_reference" ):
                listener.enterInclusive_identifier_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclusive_identifier_reference" ):
                listener.exitInclusive_identifier_reference(self)




    def inclusive_identifier_reference(self):

        localctx = PowerQueryParser.Inclusive_identifier_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_inclusive_identifier_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(PowerQueryParser.AT)
            self.state = 376
            self.match(PowerQueryParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_access_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.IDENTIFIER)
            else:
                return self.getToken(PowerQueryParser.IDENTIFIER, i)

        def BANG(self):
            return self.getToken(PowerQueryParser.BANG, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_section_access_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_access_expression" ):
                listener.enterSection_access_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_access_expression" ):
                listener.exitSection_access_expression(self)




    def section_access_expression(self):

        localctx = PowerQueryParser.Section_access_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_section_access_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(PowerQueryParser.IDENTIFIER)
            self.state = 379
            self.match(PowerQueryParser.BANG)
            self.state = 380
            self.match(PowerQueryParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parenthesized_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(PowerQueryParser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(PowerQueryParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_parenthesized_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesized_expression" ):
                listener.enterParenthesized_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesized_expression" ):
                listener.exitParenthesized_expression(self)




    def parenthesized_expression(self):

        localctx = PowerQueryParser.Parenthesized_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_parenthesized_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(PowerQueryParser.OPEN_PAREN)
            self.state = 383
            self.expression()
            self.state = 384
            self.match(PowerQueryParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_implemented_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELLIPSES(self):
            return self.getToken(PowerQueryParser.ELLIPSES, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_not_implemented_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_implemented_expression" ):
                listener.enterNot_implemented_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_implemented_expression" ):
                listener.exitNot_implemented_expression(self)




    def not_implemented_expression(self):

        localctx = PowerQueryParser.Not_implemented_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_not_implemented_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(PowerQueryParser.ELLIPSES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def argument_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Argument_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_list" ):
                listener.enterArgument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_list" ):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = PowerQueryParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_argument_list)
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.expression()
                self.state = 390
                self.match(PowerQueryParser.COMMA)
                self.state = 391
                self.argument_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(PowerQueryParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACE, 0)

        def item_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Item_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_list_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_expression" ):
                listener.enterList_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_expression" ):
                listener.exitList_expression(self)




    def list_expression(self):

        localctx = PowerQueryParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_list_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(PowerQueryParser.OPEN_BRACE)
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 2882798541774454805) != 0):
                self.state = 396
                self.item_list()


            self.state = 399
            self.match(PowerQueryParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Item_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self):
            return self.getTypedRuleContext(PowerQueryParser.ItemContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def item_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Item_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_item_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_list" ):
                listener.enterItem_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_list" ):
                listener.exitItem_list(self)




    def item_list(self):

        localctx = PowerQueryParser.Item_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_item_list)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.item()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.item()
                self.state = 403
                self.match(PowerQueryParser.COMMA)
                self.state = 404
                self.item_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,i)


        def DOTDOT(self):
            return self.getToken(PowerQueryParser.DOTDOT, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)




    def item(self):

        localctx = PowerQueryParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_item)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.expression()
                self.state = 410
                self.match(PowerQueryParser.DOTDOT)
                self.state = 411
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Record_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(PowerQueryParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACKET, 0)

        def field_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_record_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord_expression" ):
                listener.enterRecord_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord_expression" ):
                listener.exitRecord_expression(self)




    def record_expression(self):

        localctx = PowerQueryParser.Record_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_record_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==69:
                self.state = 416
                self.field_list()


            self.state = 419
            self.match(PowerQueryParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(PowerQueryParser.FieldContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def field_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_field_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_list" ):
                listener.enterField_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_list" ):
                listener.exitField_list(self)




    def field_list(self):

        localctx = PowerQueryParser.Field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_field_list)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.field()
                self.state = 423
                self.match(PowerQueryParser.COMMA)
                self.state = 424
                self.field_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_name(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_nameContext,0)


        def EQUALS(self):
            return self.getToken(PowerQueryParser.EQUALS, 0)

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)




    def field(self):

        localctx = PowerQueryParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.field_name()
            self.state = 429
            self.match(PowerQueryParser.EQUALS)
            self.state = 430
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PowerQueryParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_field_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_name" ):
                listener.enterField_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_name" ):
                listener.exitField_name(self)




    def field_name(self):

        localctx = PowerQueryParser.Field_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(PowerQueryParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Item_selectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_item_selector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_selector" ):
                listener.enterItem_selector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_selector" ):
                listener.exitItem_selector(self)




    def item_selector(self):

        localctx = PowerQueryParser.Item_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_item_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_selectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def required_field_selector(self):
            return self.getTypedRuleContext(PowerQueryParser.Required_field_selectorContext,0)


        def optional_field_selector(self):
            return self.getTypedRuleContext(PowerQueryParser.Optional_field_selectorContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_field_selector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_selector" ):
                listener.enterField_selector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_selector" ):
                listener.exitField_selector(self)




    def field_selector(self):

        localctx = PowerQueryParser.Field_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_field_selector)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.required_field_selector()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.optional_field_selector()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Required_field_selectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(PowerQueryParser.OPEN_BRACKET, 0)

        def field_name(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_nameContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_required_field_selector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequired_field_selector" ):
                listener.enterRequired_field_selector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequired_field_selector" ):
                listener.exitRequired_field_selector(self)




    def required_field_selector(self):

        localctx = PowerQueryParser.Required_field_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_required_field_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 441
            self.field_name()
            self.state = 442
            self.match(PowerQueryParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_field_selectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(PowerQueryParser.OPEN_BRACKET, 0)

        def field_name(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_nameContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACKET, 0)

        def OPTIONAL(self):
            return self.getToken(PowerQueryParser.OPTIONAL, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_optional_field_selector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_field_selector" ):
                listener.enterOptional_field_selector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_field_selector" ):
                listener.exitOptional_field_selector(self)




    def optional_field_selector(self):

        localctx = PowerQueryParser.Optional_field_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_optional_field_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 445
            self.field_name()
            self.state = 446
            self.match(PowerQueryParser.CLOSE_BRACKET)
            self.state = 447
            self.match(PowerQueryParser.OPTIONAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_target_field_selectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_selector(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_selectorContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_implicit_target_field_selection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicit_target_field_selection" ):
                listener.enterImplicit_target_field_selection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicit_target_field_selection" ):
                listener.exitImplicit_target_field_selection(self)




    def implicit_target_field_selection(self):

        localctx = PowerQueryParser.Implicit_target_field_selectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_implicit_target_field_selection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.field_selector()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Required_projectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(PowerQueryParser.OPEN_BRACKET, 0)

        def required_selector_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Required_selector_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_required_projection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequired_projection" ):
                listener.enterRequired_projection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequired_projection" ):
                listener.exitRequired_projection(self)




    def required_projection(self):

        localctx = PowerQueryParser.Required_projectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_required_projection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 452
            self.required_selector_list()
            self.state = 453
            self.match(PowerQueryParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_projectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(PowerQueryParser.OPEN_BRACKET, 0)

        def required_selector_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Required_selector_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACKET, 0)

        def OPTIONAL(self):
            return self.getToken(PowerQueryParser.OPTIONAL, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_optional_projection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_projection" ):
                listener.enterOptional_projection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_projection" ):
                listener.exitOptional_projection(self)




    def optional_projection(self):

        localctx = PowerQueryParser.Optional_projectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_optional_projection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 456
            self.required_selector_list()
            self.state = 457
            self.match(PowerQueryParser.CLOSE_BRACKET)
            self.state = 458
            self.match(PowerQueryParser.OPTIONAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Required_selector_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def required_field_selector(self):
            return self.getTypedRuleContext(PowerQueryParser.Required_field_selectorContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def required_selector_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Required_selector_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_required_selector_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequired_selector_list" ):
                listener.enterRequired_selector_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequired_selector_list" ):
                listener.exitRequired_selector_list(self)




    def required_selector_list(self):

        localctx = PowerQueryParser.Required_selector_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_required_selector_list)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.required_field_selector()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.required_field_selector()
                self.state = 462
                self.match(PowerQueryParser.COMMA)
                self.state = 463
                self.required_selector_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_target_projectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def required_projection(self):
            return self.getTypedRuleContext(PowerQueryParser.Required_projectionContext,0)


        def optional_projection(self):
            return self.getTypedRuleContext(PowerQueryParser.Optional_projectionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_implicit_target_projection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicit_target_projection" ):
                listener.enterImplicit_target_projection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicit_target_projection" ):
                listener.exitImplicit_target_projection(self)




    def implicit_target_projection(self):

        localctx = PowerQueryParser.Implicit_target_projectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_implicit_target_projection)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.required_projection()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.optional_projection()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(PowerQueryParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(PowerQueryParser.CLOSE_PAREN, 0)

        def ARROW(self):
            return self.getToken(PowerQueryParser.ARROW, 0)

        def function_body(self):
            return self.getTypedRuleContext(PowerQueryParser.Function_bodyContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Parameter_listContext,0)


        def return_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Return_typeContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_function_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_expression" ):
                listener.enterFunction_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_expression" ):
                listener.exitFunction_expression(self)




    def function_expression(self):

        localctx = PowerQueryParser.Function_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_function_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(PowerQueryParser.OPEN_PAREN)
            self.state = 473
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==69:
                self.state = 472
                self.parameter_list()


            self.state = 475
            self.match(PowerQueryParser.CLOSE_PAREN)
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 476
                self.return_type()


            self.state = 479
            self.match(PowerQueryParser.ARROW)
            self.state = 480
            self.function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_function_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_body" ):
                listener.enterFunction_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_body" ):
                listener.exitFunction_body(self)




    def function_body(self):

        localctx = PowerQueryParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_function_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fixed_parameter_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Fixed_parameter_listContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def optional_parameter_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Optional_parameter_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_list" ):
                listener.enterParameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_list" ):
                listener.exitParameter_list(self)




    def parameter_list(self):

        localctx = PowerQueryParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_parameter_list)
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.fixed_parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.fixed_parameter_list()
                self.state = 486
                self.match(PowerQueryParser.COMMA)
                self.state = 487
                self.optional_parameter_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixed_parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(PowerQueryParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def fixed_parameter_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Fixed_parameter_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_fixed_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixed_parameter_list" ):
                listener.enterFixed_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixed_parameter_list" ):
                listener.exitFixed_parameter_list(self)




    def fixed_parameter_list(self):

        localctx = PowerQueryParser.Fixed_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_fixed_parameter_list)
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.parameter()
                self.state = 493
                self.match(PowerQueryParser.COMMA)
                self.state = 494
                self.fixed_parameter_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_name(self):
            return self.getTypedRuleContext(PowerQueryParser.Parameter_nameContext,0)


        def parameter_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Parameter_typeContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = PowerQueryParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.parameter_name()
            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 499
                self.parameter_type()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PowerQueryParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_parameter_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_name" ):
                listener.enterParameter_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_name" ):
                listener.exitParameter_name(self)




    def parameter_name(self):

        localctx = PowerQueryParser.Parameter_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_parameter_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(PowerQueryParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assertion(self):
            return self.getTypedRuleContext(PowerQueryParser.AssertionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_parameter_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_type" ):
                listener.enterParameter_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_type" ):
                listener.exitParameter_type(self)




    def parameter_type(self):

        localctx = PowerQueryParser.Parameter_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_parameter_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.assertion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assertion(self):
            return self.getTypedRuleContext(PowerQueryParser.AssertionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_return_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_type" ):
                listener.enterReturn_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_type" ):
                listener.exitReturn_type(self)




    def return_type(self):

        localctx = PowerQueryParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_return_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.assertion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssertionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AS(self):
            return self.getToken(PowerQueryParser.AS, 0)

        def nullable_primitive_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Nullable_primitive_typeContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_assertion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssertion" ):
                listener.enterAssertion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssertion" ):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = PowerQueryParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(PowerQueryParser.AS)
            self.state = 509
            self.nullable_primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optional_parameter(self):
            return self.getTypedRuleContext(PowerQueryParser.Optional_parameterContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def optional_parameter_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Optional_parameter_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_optional_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_parameter_list" ):
                listener.enterOptional_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_parameter_list" ):
                listener.exitOptional_parameter_list(self)




    def optional_parameter_list(self):

        localctx = PowerQueryParser.Optional_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_optional_parameter_list)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.optional_parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.optional_parameter()
                self.state = 513
                self.match(PowerQueryParser.COMMA)
                self.state = 514
                self.optional_parameter_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTIONAL_TEXT(self):
            return self.getToken(PowerQueryParser.OPTIONAL_TEXT, 0)

        def parameter(self):
            return self.getTypedRuleContext(PowerQueryParser.ParameterContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_optional_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_parameter" ):
                listener.enterOptional_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_parameter" ):
                listener.exitOptional_parameter(self)




    def optional_parameter(self):

        localctx = PowerQueryParser.Optional_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_optional_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(PowerQueryParser.OPTIONAL_TEXT)
            self.state = 519
            self.parameter()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Each_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EACH(self):
            return self.getToken(PowerQueryParser.EACH, 0)

        def each_expression_body(self):
            return self.getTypedRuleContext(PowerQueryParser.Each_expression_bodyContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_each_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEach_expression" ):
                listener.enterEach_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEach_expression" ):
                listener.exitEach_expression(self)




    def each_expression(self):

        localctx = PowerQueryParser.Each_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_each_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(PowerQueryParser.EACH)
            self.state = 522
            self.each_expression_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Each_expression_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_body(self):
            return self.getTypedRuleContext(PowerQueryParser.Function_bodyContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_each_expression_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEach_expression_body" ):
                listener.enterEach_expression_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEach_expression_body" ):
                listener.exitEach_expression_body(self)




    def each_expression_body(self):

        localctx = PowerQueryParser.Each_expression_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_each_expression_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Let_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(PowerQueryParser.LET, 0)

        def variable_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Variable_listContext,0)


        def IN(self):
            return self.getToken(PowerQueryParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_let_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet_expression" ):
                listener.enterLet_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet_expression" ):
                listener.exitLet_expression(self)




    def let_expression(self):

        localctx = PowerQueryParser.Let_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_let_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(PowerQueryParser.LET)
            self.state = 527
            self.variable_list()
            self.state = 528
            self.match(PowerQueryParser.IN)
            self.state = 529
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PowerQueryParser.VariableContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def variable_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Variable_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_variable_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_list" ):
                listener.enterVariable_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_list" ):
                listener.exitVariable_list(self)




    def variable_list(self):

        localctx = PowerQueryParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_variable_list)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.variable()
                self.state = 533
                self.match(PowerQueryParser.COMMA)
                self.state = 534
                self.variable_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_name(self):
            return self.getTypedRuleContext(PowerQueryParser.Variable_nameContext,0)


        def EQUALS(self):
            return self.getToken(PowerQueryParser.EQUALS, 0)

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = PowerQueryParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.variable_name()
            self.state = 539
            self.match(PowerQueryParser.EQUALS)
            self.state = 540
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PowerQueryParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_variable_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_name" ):
                listener.enterVariable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_name" ):
                listener.exitVariable_name(self)




    def variable_name(self):

        localctx = PowerQueryParser.Variable_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_variable_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(PowerQueryParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PowerQueryParser.IF, 0)

        def if_condition(self):
            return self.getTypedRuleContext(PowerQueryParser.If_conditionContext,0)


        def THEN(self):
            return self.getToken(PowerQueryParser.THEN, 0)

        def true_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.True_expressionContext,0)


        def ELSE(self):
            return self.getToken(PowerQueryParser.ELSE, 0)

        def false_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.False_expressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_if_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_expression" ):
                listener.enterIf_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_expression" ):
                listener.exitIf_expression(self)




    def if_expression(self):

        localctx = PowerQueryParser.If_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_if_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(PowerQueryParser.IF)
            self.state = 545
            self.if_condition()
            self.state = 546
            self.match(PowerQueryParser.THEN)
            self.state = 547
            self.true_expression()
            self.state = 548
            self.match(PowerQueryParser.ELSE)
            self.state = 549
            self.false_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_if_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_condition" ):
                listener.enterIf_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_condition" ):
                listener.exitIf_condition(self)




    def if_condition(self):

        localctx = PowerQueryParser.If_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_if_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class True_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_true_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue_expression" ):
                listener.enterTrue_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue_expression" ):
                listener.exitTrue_expression(self)




    def true_expression(self):

        localctx = PowerQueryParser.True_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_true_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class False_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_false_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalse_expression" ):
                listener.enterFalse_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalse_expression" ):
                listener.exitFalse_expression(self)




    def false_expression(self):

        localctx = PowerQueryParser.False_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_false_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Primary_expressionContext,0)


        def TYPE(self):
            return self.getToken(PowerQueryParser.TYPE, 0)

        def primary_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Primary_typeContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_type_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_expression" ):
                listener.enterType_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_expression" ):
                listener.exitType_expression(self)




    def type_expression(self):

        localctx = PowerQueryParser.Type_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_type_expression)
        try:
            self.state = 560
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 10, 12, 27, 49, 67, 69]:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.primary_expression()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 558
                self.match(PowerQueryParser.TYPE)
                self.state = 559
                self.primary_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parenthesized_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Parenthesized_expressionContext,0)


        def primary_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Primary_typeContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_type_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_expr" ):
                listener.enterType_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_expr" ):
                listener.exitType_expr(self)




    def type_expr(self):

        localctx = PowerQueryParser.Type_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_type_expr)
        try:
            self.state = 564
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 562
                self.parenthesized_expression()
                pass
            elif token in [8, 10, 16, 17, 26, 28, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 67]:
                self.enterOuterAlt(localctx, 2)
                self.state = 563
                self.primary_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Primitive_typeContext,0)


        def record_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Record_typeContext,0)


        def list_type(self):
            return self.getTypedRuleContext(PowerQueryParser.List_typeContext,0)


        def function_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Function_typeContext,0)


        def table_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Table_typeContext,0)


        def nullable_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Nullable_typeContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_primary_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_type" ):
                listener.enterPrimary_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_type" ):
                listener.exitPrimary_type(self)




    def primary_type(self):

        localctx = PowerQueryParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_primary_type)
        try:
            self.state = 572
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 567
                self.record_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 568
                self.list_type()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 569
                self.function_type()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 570
                self.table_type()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 571
                self.nullable_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANY(self):
            return self.getToken(PowerQueryParser.ANY, 0)

        def ANYNONNULL(self):
            return self.getToken(PowerQueryParser.ANYNONNULL, 0)

        def BINARY(self):
            return self.getToken(PowerQueryParser.BINARY, 0)

        def DATE(self):
            return self.getToken(PowerQueryParser.DATE, 0)

        def DATETIME(self):
            return self.getToken(PowerQueryParser.DATETIME, 0)

        def DATETIMEZONE(self):
            return self.getToken(PowerQueryParser.DATETIMEZONE, 0)

        def DURATION(self):
            return self.getToken(PowerQueryParser.DURATION, 0)

        def FUNCTION(self):
            return self.getToken(PowerQueryParser.FUNCTION, 0)

        def LIST(self):
            return self.getToken(PowerQueryParser.LIST, 0)

        def LOGICAL(self):
            return self.getToken(PowerQueryParser.LOGICAL, 0)

        def NONE(self):
            return self.getToken(PowerQueryParser.NONE, 0)

        def NUMBER(self):
            return self.getToken(PowerQueryParser.NUMBER, 0)

        def RECORD(self):
            return self.getToken(PowerQueryParser.RECORD, 0)

        def TABLE(self):
            return self.getToken(PowerQueryParser.TABLE, 0)

        def TEXT(self):
            return self.getToken(PowerQueryParser.TEXT, 0)

        def TYPE(self):
            return self.getToken(PowerQueryParser.TYPE, 0)

        def LITERAL(self):
            return self.getToken(PowerQueryParser.LITERAL, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_primitive_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive_type" ):
                listener.enterPrimitive_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive_type" ):
                listener.exitPrimitive_type(self)




    def primitive_type(self):

        localctx = PowerQueryParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            _la = self._input.LA(1)
            if not(((((_la - 16)) & ~0x3f) == 0 and ((1 << (_la - 16)) & 2251808403099649) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Record_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(PowerQueryParser.OPEN_BRACKET, 0)

        def open_record_marker(self):
            return self.getTypedRuleContext(PowerQueryParser.Open_record_markerContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACKET, 0)

        def field_specification_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_specification_listContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_record_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord_type" ):
                listener.enterRecord_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord_type" ):
                listener.exitRecord_type(self)




    def record_type(self):

        localctx = PowerQueryParser.Record_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_record_type)
        self._la = 0 # Token type
        try:
            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.match(PowerQueryParser.OPEN_BRACKET)
                self.state = 577
                self.open_record_marker()
                self.state = 578
                self.match(PowerQueryParser.CLOSE_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 580
                self.match(PowerQueryParser.OPEN_BRACKET)
                self.state = 582
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15 or _la==69:
                    self.state = 581
                    self.field_specification_list()


                self.state = 584
                self.match(PowerQueryParser.CLOSE_BRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 585
                self.match(PowerQueryParser.OPEN_BRACKET)
                self.state = 586
                self.field_specification_list()
                self.state = 587
                self.match(PowerQueryParser.COMMA)
                self.state = 588
                self.open_record_marker()
                self.state = 589
                self.match(PowerQueryParser.CLOSE_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_specification_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_specification(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_specificationContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def field_specification_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_specification_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_field_specification_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_specification_list" ):
                listener.enterField_specification_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_specification_list" ):
                listener.exitField_specification_list(self)




    def field_specification_list(self):

        localctx = PowerQueryParser.Field_specification_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_field_specification_list)
        try:
            self.state = 598
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 593
                self.field_specification()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 594
                self.field_specification()
                self.state = 595
                self.match(PowerQueryParser.COMMA)
                self.state = 596
                self.field_specification_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_specificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_name(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_nameContext,0)


        def OPTIONAL_TEXT(self):
            return self.getToken(PowerQueryParser.OPTIONAL_TEXT, 0)

        def field_type_specification(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_type_specificationContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_field_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_specification" ):
                listener.enterField_specification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_specification" ):
                listener.exitField_specification(self)




    def field_specification(self):

        localctx = PowerQueryParser.Field_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_field_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 600
                self.match(PowerQueryParser.OPTIONAL_TEXT)


            self.state = 603
            self.field_name()
            self.state = 605
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 604
                self.field_type_specification()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_type_specificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(PowerQueryParser.EQUALS, 0)

        def field_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_typeContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_field_type_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_type_specification" ):
                listener.enterField_type_specification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_type_specification" ):
                listener.exitField_type_specification(self)




    def field_type_specification(self):

        localctx = PowerQueryParser.Field_type_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_field_type_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.match(PowerQueryParser.EQUALS)
            self.state = 608
            self.field_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_expr(self):
            return self.getTypedRuleContext(PowerQueryParser.Type_exprContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_field_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_type" ):
                listener.enterField_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_type" ):
                listener.exitField_type(self)




    def field_type(self):

        localctx = PowerQueryParser.Field_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_field_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 610
            self.type_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Open_record_markerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELLIPSES(self):
            return self.getToken(PowerQueryParser.ELLIPSES, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_open_record_marker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpen_record_marker" ):
                listener.enterOpen_record_marker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpen_record_marker" ):
                listener.exitOpen_record_marker(self)




    def open_record_marker(self):

        localctx = PowerQueryParser.Open_record_markerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_open_record_marker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.match(PowerQueryParser.ELLIPSES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(PowerQueryParser.OPEN_BRACE, 0)

        def item_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Item_typeContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_list_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_type" ):
                listener.enterList_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_type" ):
                listener.exitList_type(self)




    def list_type(self):

        localctx = PowerQueryParser.List_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.match(PowerQueryParser.OPEN_BRACE)
            self.state = 615
            self.item_type()
            self.state = 616
            self.match(PowerQueryParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Item_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_expr(self):
            return self.getTypedRuleContext(PowerQueryParser.Type_exprContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_item_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_type" ):
                listener.enterItem_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_type" ):
                listener.exitItem_type(self)




    def item_type(self):

        localctx = PowerQueryParser.Item_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_item_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            self.type_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_START(self):
            return self.getToken(PowerQueryParser.FUNCTION_START, 0)

        def CLOSE_PAREN(self):
            return self.getToken(PowerQueryParser.CLOSE_PAREN, 0)

        def return_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Return_typeContext,0)


        def parameter_specification_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Parameter_specification_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_function_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_type" ):
                listener.enterFunction_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_type" ):
                listener.exitFunction_type(self)




    def function_type(self):

        localctx = PowerQueryParser.Function_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_function_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self.match(PowerQueryParser.FUNCTION_START)
            self.state = 622
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15 or _la==69:
                self.state = 621
                self.parameter_specification_list()


            self.state = 624
            self.match(PowerQueryParser.CLOSE_PAREN)
            self.state = 625
            self.return_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_specification_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def required_parameter_specification_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Required_parameter_specification_listContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def optional_parameter_specification_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Optional_parameter_specification_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_parameter_specification_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_specification_list" ):
                listener.enterParameter_specification_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_specification_list" ):
                listener.exitParameter_specification_list(self)




    def parameter_specification_list(self):

        localctx = PowerQueryParser.Parameter_specification_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_parameter_specification_list)
        try:
            self.state = 633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 627
                self.required_parameter_specification_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 628
                self.required_parameter_specification_list()
                self.state = 629
                self.match(PowerQueryParser.COMMA)
                self.state = 630
                self.optional_parameter_specification_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 632
                self.optional_parameter_specification_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Required_parameter_specification_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def required_parameter_specification(self):
            return self.getTypedRuleContext(PowerQueryParser.Required_parameter_specificationContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def required_parameter_specification_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Required_parameter_specification_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_required_parameter_specification_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequired_parameter_specification_list" ):
                listener.enterRequired_parameter_specification_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequired_parameter_specification_list" ):
                listener.exitRequired_parameter_specification_list(self)




    def required_parameter_specification_list(self):

        localctx = PowerQueryParser.Required_parameter_specification_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_required_parameter_specification_list)
        try:
            self.state = 640
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 635
                self.required_parameter_specification()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 636
                self.required_parameter_specification()
                self.state = 637
                self.match(PowerQueryParser.COMMA)
                self.state = 638
                self.required_parameter_specification_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Required_parameter_specificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_specification(self):
            return self.getTypedRuleContext(PowerQueryParser.Parameter_specificationContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_required_parameter_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequired_parameter_specification" ):
                listener.enterRequired_parameter_specification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequired_parameter_specification" ):
                listener.exitRequired_parameter_specification(self)




    def required_parameter_specification(self):

        localctx = PowerQueryParser.Required_parameter_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_required_parameter_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
            self.parameter_specification()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_parameter_specification_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optional_parameter_specification(self):
            return self.getTypedRuleContext(PowerQueryParser.Optional_parameter_specificationContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def optional_parameter_specification_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Optional_parameter_specification_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_optional_parameter_specification_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_parameter_specification_list" ):
                listener.enterOptional_parameter_specification_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_parameter_specification_list" ):
                listener.exitOptional_parameter_specification_list(self)




    def optional_parameter_specification_list(self):

        localctx = PowerQueryParser.Optional_parameter_specification_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_optional_parameter_specification_list)
        try:
            self.state = 649
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 644
                self.optional_parameter_specification()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 645
                self.optional_parameter_specification()
                self.state = 646
                self.match(PowerQueryParser.COMMA)
                self.state = 647
                self.optional_parameter_specification_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_parameter_specificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTIONAL_TEXT(self):
            return self.getToken(PowerQueryParser.OPTIONAL_TEXT, 0)

        def parameter_specification(self):
            return self.getTypedRuleContext(PowerQueryParser.Parameter_specificationContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_optional_parameter_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_parameter_specification" ):
                listener.enterOptional_parameter_specification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_parameter_specification" ):
                listener.exitOptional_parameter_specification(self)




    def optional_parameter_specification(self):

        localctx = PowerQueryParser.Optional_parameter_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_optional_parameter_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            self.match(PowerQueryParser.OPTIONAL_TEXT)
            self.state = 652
            self.parameter_specification()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_specificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_name(self):
            return self.getTypedRuleContext(PowerQueryParser.Parameter_nameContext,0)


        def parameter_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Parameter_typeContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_parameter_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_specification" ):
                listener.enterParameter_specification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_specification" ):
                listener.exitParameter_specification(self)




    def parameter_specification(self):

        localctx = PowerQueryParser.Parameter_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_parameter_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.parameter_name()
            self.state = 655
            self.parameter_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TABLE(self):
            return self.getToken(PowerQueryParser.TABLE, 0)

        def row_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Row_typeContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_table_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_type" ):
                listener.enterTable_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_type" ):
                listener.exitTable_type(self)




    def table_type(self):

        localctx = PowerQueryParser.Table_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_table_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 657
            self.match(PowerQueryParser.TABLE)
            self.state = 658
            self.row_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Row_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(PowerQueryParser.OPEN_BRACKET, 0)

        def field_specification_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_specification_listContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_row_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow_type" ):
                listener.enterRow_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow_type" ):
                listener.exitRow_type(self)




    def row_type(self):

        localctx = PowerQueryParser.Row_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_row_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 661
            self.field_specification_list()
            self.state = 662
            self.match(PowerQueryParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULLABLE(self):
            return self.getToken(PowerQueryParser.NULLABLE, 0)

        def type_expr(self):
            return self.getTypedRuleContext(PowerQueryParser.Type_exprContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_nullable_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullable_type" ):
                listener.enterNullable_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullable_type" ):
                listener.exitNullable_type(self)




    def nullable_type(self):

        localctx = PowerQueryParser.Nullable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_nullable_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 664
            self.match(PowerQueryParser.NULLABLE)
            self.state = 665
            self.type_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Error_raising_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ERROR(self):
            return self.getToken(PowerQueryParser.ERROR, 0)

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_error_raising_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterError_raising_expression" ):
                listener.enterError_raising_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitError_raising_expression" ):
                listener.exitError_raising_expression(self)




    def error_raising_expression(self):

        localctx = PowerQueryParser.Error_raising_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_error_raising_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.match(PowerQueryParser.ERROR)
            self.state = 668
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Error_handling_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(PowerQueryParser.TRY, 0)

        def protected_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Protected_expressionContext,0)


        def otherwise_clause(self):
            return self.getTypedRuleContext(PowerQueryParser.Otherwise_clauseContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_error_handling_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterError_handling_expression" ):
                listener.enterError_handling_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitError_handling_expression" ):
                listener.exitError_handling_expression(self)




    def error_handling_expression(self):

        localctx = PowerQueryParser.Error_handling_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_error_handling_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 670
            self.match(PowerQueryParser.TRY)
            self.state = 671
            self.protected_expression()
            self.state = 673
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 672
                self.otherwise_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Protected_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_protected_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtected_expression" ):
                listener.enterProtected_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtected_expression" ):
                listener.exitProtected_expression(self)




    def protected_expression(self):

        localctx = PowerQueryParser.Protected_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_protected_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Otherwise_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OTHERWISE(self):
            return self.getToken(PowerQueryParser.OTHERWISE, 0)

        def default_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Default_expressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_otherwise_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOtherwise_clause" ):
                listener.enterOtherwise_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOtherwise_clause" ):
                listener.exitOtherwise_clause(self)




    def otherwise_clause(self):

        localctx = PowerQueryParser.Otherwise_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_otherwise_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
            self.match(PowerQueryParser.OTHERWISE)
            self.state = 678
            self.default_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Default_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_default_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefault_expression" ):
                listener.enterDefault_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefault_expression" ):
                listener.exitDefault_expression(self)




    def default_expression(self):

        localctx = PowerQueryParser.Default_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_default_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_attribsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def record_literal(self):
            return self.getTypedRuleContext(PowerQueryParser.Record_literalContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_literal_attribs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_attribs" ):
                listener.enterLiteral_attribs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_attribs" ):
                listener.exitLiteral_attribs(self)




    def literal_attribs(self):

        localctx = PowerQueryParser.Literal_attribsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_literal_attribs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
            self.record_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Record_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(PowerQueryParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACKET, 0)

        def literal_field_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Literal_field_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_record_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord_literal" ):
                listener.enterRecord_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord_literal" ):
                listener.exitRecord_literal(self)




    def record_literal(self):

        localctx = PowerQueryParser.Record_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_record_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 686
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==69:
                self.state = 685
                self.literal_field_list()


            self.state = 688
            self.match(PowerQueryParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_field(self):
            return self.getTypedRuleContext(PowerQueryParser.Literal_fieldContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def literal_field_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Literal_field_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_literal_field_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_field_list" ):
                listener.enterLiteral_field_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_field_list" ):
                listener.exitLiteral_field_list(self)




    def literal_field_list(self):

        localctx = PowerQueryParser.Literal_field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_literal_field_list)
        try:
            self.state = 695
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 690
                self.literal_field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 691
                self.literal_field()
                self.state = 692
                self.match(PowerQueryParser.COMMA)
                self.state = 693
                self.literal_field_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_name(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_nameContext,0)


        def EQUALS(self):
            return self.getToken(PowerQueryParser.EQUALS, 0)

        def any_literal(self):
            return self.getTypedRuleContext(PowerQueryParser.Any_literalContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_literal_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_field" ):
                listener.enterLiteral_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_field" ):
                listener.exitLiteral_field(self)




    def literal_field(self):

        localctx = PowerQueryParser.Literal_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_literal_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 697
            self.field_name()
            self.state = 698
            self.match(PowerQueryParser.EQUALS)
            self.state = 699
            self.any_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(PowerQueryParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACE, 0)

        def literal_item_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Literal_item_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_list_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_literal" ):
                listener.enterList_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_literal" ):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = PowerQueryParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 701
            self.match(PowerQueryParser.OPEN_BRACE)
            self.state = 703
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 576460752303423493) != 0):
                self.state = 702
                self.literal_item_list()


            self.state = 705
            self.match(PowerQueryParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_item_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_literal(self):
            return self.getTypedRuleContext(PowerQueryParser.Any_literalContext,0)


        def COMMA(self):
            return self.getToken(PowerQueryParser.COMMA, 0)

        def literal_item_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Literal_item_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_literal_item_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_item_list" ):
                listener.enterLiteral_item_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_item_list" ):
                listener.exitLiteral_item_list(self)




    def literal_item_list(self):

        localctx = PowerQueryParser.Literal_item_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_literal_item_list)
        try:
            self.state = 712
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 707
                self.any_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 708
                self.any_literal()
                self.state = 709
                self.match(PowerQueryParser.COMMA)
                self.state = 710
                self.literal_item_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def record_literal(self):
            return self.getTypedRuleContext(PowerQueryParser.Record_literalContext,0)


        def list_literal(self):
            return self.getTypedRuleContext(PowerQueryParser.List_literalContext,0)


        def LITERAL(self):
            return self.getToken(PowerQueryParser.LITERAL, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_any_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_literal" ):
                listener.enterAny_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_literal" ):
                listener.exitAny_literal(self)




    def any_literal(self):

        localctx = PowerQueryParser.Any_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_any_literal)
        try:
            self.state = 717
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 714
                self.record_literal()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 715
                self.list_literal()
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 3)
                self.state = 716
                self.match(PowerQueryParser.LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





