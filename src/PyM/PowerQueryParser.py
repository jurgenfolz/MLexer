# Generated from src/PyM/PowerQueryParser.g4 by ANTLR 4.10.1
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
        4,1,71,760,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        7,98,2,99,7,99,2,100,7,100,1,0,1,0,3,0,205,8,0,1,1,1,1,1,2,3,2,210,
        8,2,1,2,1,2,1,2,1,2,3,2,216,8,2,1,3,1,3,1,4,1,4,3,4,222,8,4,1,5,
        3,5,225,8,5,1,5,3,5,228,8,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,247,8,8,1,9,1,9,1,9,1,9,1,9,
        3,9,254,8,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,262,8,10,10,10,12,
        10,265,9,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,273,8,11,10,11,12,
        11,276,9,11,1,12,3,12,279,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,5,13,289,8,13,10,13,12,13,292,9,13,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,3,14,303,8,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,322,
        8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,3,16,337,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        3,17,348,8,17,1,18,1,18,1,18,1,18,1,18,3,18,355,8,18,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,3,19,364,8,19,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,3,20,376,8,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,3,20,398,8,20,1,20,5,20,401,8,20,10,20,12,20,404,9,20,1,
        21,1,21,1,22,1,22,1,23,1,23,3,23,412,8,23,1,24,1,24,1,25,1,25,1,
        25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,29,1,29,1,
        29,1,29,1,29,3,29,434,8,29,1,30,1,30,3,30,438,8,30,1,30,1,30,1,31,
        1,31,1,31,1,31,1,31,3,31,447,8,31,1,32,1,32,1,32,1,32,1,32,3,32,
        454,8,32,1,33,1,33,3,33,458,8,33,1,33,1,33,1,34,1,34,1,34,1,34,1,
        34,3,34,467,8,34,1,35,1,35,1,35,1,35,1,36,1,36,1,37,1,37,1,38,1,
        38,3,38,479,8,38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,
        41,1,41,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,
        44,1,44,1,44,3,44,506,8,44,1,45,1,45,3,45,510,8,45,1,46,1,46,3,46,
        514,8,46,1,46,1,46,3,46,518,8,46,1,46,1,46,1,46,1,47,1,47,1,48,1,
        48,1,48,1,48,1,48,3,48,530,8,48,1,49,1,49,1,49,1,49,1,49,3,49,537,
        8,49,1,50,1,50,3,50,541,8,50,1,51,1,51,1,52,1,52,1,53,1,53,1,54,
        1,54,1,54,1,55,1,55,1,55,1,55,1,55,3,55,557,8,55,1,56,1,56,1,56,
        1,57,1,57,1,57,1,58,1,58,1,59,1,59,1,59,1,59,1,59,1,60,1,60,1,60,
        1,60,1,60,3,60,577,8,60,1,61,1,61,1,61,1,61,1,62,1,62,1,63,1,63,
        1,63,1,63,1,63,1,63,1,63,1,64,1,64,1,65,1,65,1,66,1,66,1,67,1,67,
        1,67,3,67,601,8,67,1,68,1,68,3,68,605,8,68,1,69,1,69,1,69,1,69,1,
        69,1,69,3,69,613,8,69,1,70,1,70,1,71,1,71,1,71,1,71,1,71,1,71,3,
        71,623,8,71,1,71,1,71,1,71,1,71,1,71,1,71,1,71,3,71,632,8,71,1,72,
        1,72,1,72,1,72,1,72,3,72,639,8,72,1,73,3,73,642,8,73,1,73,1,73,3,
        73,646,8,73,1,74,1,74,1,74,1,75,1,75,1,76,1,76,1,77,1,77,1,77,1,
        77,1,78,1,78,1,79,1,79,3,79,663,8,79,1,79,1,79,1,79,1,80,1,80,1,
        80,1,80,1,80,1,80,3,80,674,8,80,1,81,1,81,1,81,1,81,1,81,3,81,681,
        8,81,1,82,1,82,1,83,1,83,1,83,1,83,1,83,3,83,690,8,83,1,84,1,84,
        1,84,1,85,1,85,1,85,1,86,1,86,1,86,1,87,1,87,1,87,1,87,1,88,1,88,
        1,88,1,89,1,89,1,89,1,90,1,90,1,90,3,90,714,8,90,1,91,1,91,1,92,
        1,92,1,92,1,93,1,93,1,94,1,94,1,95,1,95,3,95,727,8,95,1,95,1,95,
        1,96,1,96,1,96,1,96,1,96,3,96,736,8,96,1,97,1,97,1,97,1,97,1,98,
        1,98,3,98,744,8,98,1,98,1,98,1,99,1,99,1,99,1,99,1,99,3,99,753,8,
        99,1,100,1,100,1,100,3,100,758,8,100,1,100,0,4,20,22,26,40,101,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,
        92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,
        126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,
        158,160,162,164,166,168,170,172,174,176,178,180,182,184,186,188,
        190,192,194,196,198,200,0,1,4,0,15,15,27,27,34,47,66,66,748,0,204,
        1,0,0,0,2,206,1,0,0,0,4,209,1,0,0,0,6,217,1,0,0,0,8,219,1,0,0,0,
        10,224,1,0,0,0,12,234,1,0,0,0,14,236,1,0,0,0,16,246,1,0,0,0,18,253,
        1,0,0,0,20,255,1,0,0,0,22,266,1,0,0,0,24,278,1,0,0,0,26,282,1,0,
        0,0,28,302,1,0,0,0,30,321,1,0,0,0,32,336,1,0,0,0,34,347,1,0,0,0,
        36,354,1,0,0,0,38,363,1,0,0,0,40,375,1,0,0,0,42,405,1,0,0,0,44,407,
        1,0,0,0,46,411,1,0,0,0,48,413,1,0,0,0,50,415,1,0,0,0,52,418,1,0,
        0,0,54,422,1,0,0,0,56,426,1,0,0,0,58,433,1,0,0,0,60,435,1,0,0,0,
        62,446,1,0,0,0,64,453,1,0,0,0,66,455,1,0,0,0,68,466,1,0,0,0,70,468,
        1,0,0,0,72,472,1,0,0,0,74,474,1,0,0,0,76,478,1,0,0,0,78,480,1,0,
        0,0,80,484,1,0,0,0,82,489,1,0,0,0,84,491,1,0,0,0,86,495,1,0,0,0,
        88,505,1,0,0,0,90,509,1,0,0,0,92,511,1,0,0,0,94,522,1,0,0,0,96,529,
        1,0,0,0,98,536,1,0,0,0,100,538,1,0,0,0,102,542,1,0,0,0,104,544,1,
        0,0,0,106,546,1,0,0,0,108,548,1,0,0,0,110,556,1,0,0,0,112,558,1,
        0,0,0,114,561,1,0,0,0,116,564,1,0,0,0,118,566,1,0,0,0,120,576,1,
        0,0,0,122,578,1,0,0,0,124,582,1,0,0,0,126,584,1,0,0,0,128,591,1,
        0,0,0,130,593,1,0,0,0,132,595,1,0,0,0,134,600,1,0,0,0,136,604,1,
        0,0,0,138,612,1,0,0,0,140,614,1,0,0,0,142,631,1,0,0,0,144,638,1,
        0,0,0,146,641,1,0,0,0,148,647,1,0,0,0,150,650,1,0,0,0,152,652,1,
        0,0,0,154,654,1,0,0,0,156,658,1,0,0,0,158,660,1,0,0,0,160,673,1,
        0,0,0,162,680,1,0,0,0,164,682,1,0,0,0,166,689,1,0,0,0,168,691,1,
        0,0,0,170,694,1,0,0,0,172,697,1,0,0,0,174,700,1,0,0,0,176,704,1,
        0,0,0,178,707,1,0,0,0,180,710,1,0,0,0,182,715,1,0,0,0,184,717,1,
        0,0,0,186,720,1,0,0,0,188,722,1,0,0,0,190,724,1,0,0,0,192,735,1,
        0,0,0,194,737,1,0,0,0,196,741,1,0,0,0,198,752,1,0,0,0,200,757,1,
        0,0,0,202,205,3,2,1,0,203,205,3,14,7,0,204,202,1,0,0,0,204,203,1,
        0,0,0,205,1,1,0,0,0,206,207,3,4,2,0,207,3,1,0,0,0,208,210,3,188,
        94,0,209,208,1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,212,5,18,
        0,0,212,213,3,6,3,0,213,215,5,17,0,0,214,216,3,8,4,0,215,214,1,0,
        0,0,215,216,1,0,0,0,216,5,1,0,0,0,217,218,5,68,0,0,218,7,1,0,0,0,
        219,221,3,10,5,0,220,222,3,8,4,0,221,220,1,0,0,0,221,222,1,0,0,0,
        222,9,1,0,0,0,223,225,3,188,94,0,224,223,1,0,0,0,224,225,1,0,0,0,
        225,227,1,0,0,0,226,228,5,19,0,0,227,226,1,0,0,0,227,228,1,0,0,0,
        228,229,1,0,0,0,229,230,3,12,6,0,230,231,5,5,0,0,231,232,3,16,8,
        0,232,233,5,17,0,0,233,11,1,0,0,0,234,235,5,68,0,0,235,13,1,0,0,
        0,236,237,3,16,8,0,237,15,1,0,0,0,238,247,3,18,9,0,239,247,3,114,
        57,0,240,247,3,92,46,0,241,247,3,118,59,0,242,247,3,126,63,0,243,
        247,3,118,59,0,244,247,3,178,89,0,245,247,3,180,90,0,246,238,1,0,
        0,0,246,239,1,0,0,0,246,240,1,0,0,0,246,241,1,0,0,0,246,242,1,0,
        0,0,246,243,1,0,0,0,246,244,1,0,0,0,246,245,1,0,0,0,247,17,1,0,0,
        0,248,254,3,20,10,0,249,250,3,20,10,0,250,251,5,21,0,0,251,252,3,
        18,9,0,252,254,1,0,0,0,253,248,1,0,0,0,253,249,1,0,0,0,254,19,1,
        0,0,0,255,256,6,10,-1,0,256,257,3,22,11,0,257,263,1,0,0,0,258,259,
        10,1,0,0,259,260,5,20,0,0,260,262,3,22,11,0,261,258,1,0,0,0,262,
        265,1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,264,21,1,0,0,0,265,263,
        1,0,0,0,266,267,6,11,-1,0,267,268,3,26,13,0,268,274,1,0,0,0,269,
        270,10,1,0,0,270,271,5,57,0,0,271,273,3,24,12,0,272,269,1,0,0,0,
        273,276,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,23,1,0,0,0,276,
        274,1,0,0,0,277,279,5,16,0,0,278,277,1,0,0,0,278,279,1,0,0,0,279,
        280,1,0,0,0,280,281,3,140,70,0,281,25,1,0,0,0,282,283,6,13,-1,0,
        283,284,3,28,14,0,284,290,1,0,0,0,285,286,10,1,0,0,286,287,5,49,
        0,0,287,289,3,24,12,0,288,285,1,0,0,0,289,292,1,0,0,0,290,288,1,
        0,0,0,290,291,1,0,0,0,291,27,1,0,0,0,292,290,1,0,0,0,293,303,3,30,
        15,0,294,295,3,30,15,0,295,296,5,5,0,0,296,297,3,28,14,0,297,303,
        1,0,0,0,298,299,3,30,15,0,299,300,5,58,0,0,300,301,3,28,14,0,301,
        303,1,0,0,0,302,293,1,0,0,0,302,294,1,0,0,0,302,298,1,0,0,0,303,
        29,1,0,0,0,304,322,3,32,16,0,305,306,3,32,16,0,306,307,5,60,0,0,
        307,308,3,30,15,0,308,322,1,0,0,0,309,310,3,32,16,0,310,311,5,59,
        0,0,311,312,3,30,15,0,312,322,1,0,0,0,313,314,3,32,16,0,314,315,
        5,64,0,0,315,316,3,32,16,0,316,322,1,0,0,0,317,318,3,32,16,0,318,
        319,5,65,0,0,319,320,3,30,15,0,320,322,1,0,0,0,321,304,1,0,0,0,321,
        305,1,0,0,0,321,309,1,0,0,0,321,313,1,0,0,0,321,317,1,0,0,0,322,
        31,1,0,0,0,323,337,3,34,17,0,324,325,3,34,17,0,325,326,5,54,0,0,
        326,327,3,32,16,0,327,337,1,0,0,0,328,329,3,34,17,0,329,330,5,55,
        0,0,330,331,3,32,16,0,331,337,1,0,0,0,332,333,3,34,17,0,333,334,
        5,63,0,0,334,335,3,32,16,0,335,337,1,0,0,0,336,323,1,0,0,0,336,324,
        1,0,0,0,336,328,1,0,0,0,336,332,1,0,0,0,337,33,1,0,0,0,338,348,3,
        36,18,0,339,340,3,36,18,0,340,341,5,62,0,0,341,342,3,34,17,0,342,
        348,1,0,0,0,343,344,3,36,18,0,344,345,5,61,0,0,345,346,3,34,17,0,
        346,348,1,0,0,0,347,338,1,0,0,0,347,339,1,0,0,0,347,343,1,0,0,0,
        348,35,1,0,0,0,349,355,3,38,19,0,350,351,3,38,19,0,351,352,5,56,
        0,0,352,353,3,38,19,0,353,355,1,0,0,0,354,349,1,0,0,0,354,350,1,
        0,0,0,355,37,1,0,0,0,356,364,3,134,67,0,357,358,5,54,0,0,358,364,
        3,38,19,0,359,360,5,55,0,0,360,364,3,38,19,0,361,362,5,53,0,0,362,
        364,3,38,19,0,363,356,1,0,0,0,363,357,1,0,0,0,363,359,1,0,0,0,363,
        361,1,0,0,0,364,39,1,0,0,0,365,366,6,20,-1,0,366,376,3,42,21,0,367,
        376,3,60,30,0,368,376,3,66,33,0,369,376,3,44,22,0,370,376,3,52,26,
        0,371,376,3,54,27,0,372,376,3,82,41,0,373,376,3,90,45,0,374,376,
        3,56,28,0,375,365,1,0,0,0,375,367,1,0,0,0,375,368,1,0,0,0,375,369,
        1,0,0,0,375,370,1,0,0,0,375,371,1,0,0,0,375,372,1,0,0,0,375,373,
        1,0,0,0,375,374,1,0,0,0,376,402,1,0,0,0,377,378,10,9,0,0,378,401,
        3,76,38,0,379,380,10,7,0,0,380,401,3,84,42,0,381,382,10,6,0,0,382,
        401,3,86,43,0,383,384,10,4,0,0,384,385,5,9,0,0,385,386,3,74,37,0,
        386,387,5,10,0,0,387,401,1,0,0,0,388,389,10,3,0,0,389,390,5,9,0,
        0,390,391,3,74,37,0,391,392,5,10,0,0,392,393,5,13,0,0,393,401,1,
        0,0,0,394,395,10,2,0,0,395,397,5,11,0,0,396,398,3,58,29,0,397,396,
        1,0,0,0,397,398,1,0,0,0,398,399,1,0,0,0,399,401,5,12,0,0,400,377,
        1,0,0,0,400,379,1,0,0,0,400,381,1,0,0,0,400,383,1,0,0,0,400,388,
        1,0,0,0,400,394,1,0,0,0,401,404,1,0,0,0,402,400,1,0,0,0,402,403,
        1,0,0,0,403,41,1,0,0,0,404,402,1,0,0,0,405,406,5,66,0,0,406,43,1,
        0,0,0,407,408,3,46,23,0,408,45,1,0,0,0,409,412,3,48,24,0,410,412,
        3,50,25,0,411,409,1,0,0,0,411,410,1,0,0,0,412,47,1,0,0,0,413,414,
        5,68,0,0,414,49,1,0,0,0,415,416,5,48,0,0,416,417,5,68,0,0,417,51,
        1,0,0,0,418,419,5,68,0,0,419,420,5,52,0,0,420,421,5,68,0,0,421,53,
        1,0,0,0,422,423,5,11,0,0,423,424,3,16,8,0,424,425,5,12,0,0,425,55,
        1,0,0,0,426,427,5,26,0,0,427,57,1,0,0,0,428,434,3,16,8,0,429,430,
        3,16,8,0,430,431,5,6,0,0,431,432,3,58,29,0,432,434,1,0,0,0,433,428,
        1,0,0,0,433,429,1,0,0,0,434,59,1,0,0,0,435,437,5,9,0,0,436,438,3,
        62,31,0,437,436,1,0,0,0,437,438,1,0,0,0,438,439,1,0,0,0,439,440,
        5,10,0,0,440,61,1,0,0,0,441,447,3,64,32,0,442,443,3,64,32,0,443,
        444,5,6,0,0,444,445,3,62,31,0,445,447,1,0,0,0,446,441,1,0,0,0,446,
        442,1,0,0,0,447,63,1,0,0,0,448,454,3,16,8,0,449,450,3,16,8,0,450,
        451,5,51,0,0,451,452,3,16,8,0,452,454,1,0,0,0,453,448,1,0,0,0,453,
        449,1,0,0,0,454,65,1,0,0,0,455,457,5,7,0,0,456,458,3,68,34,0,457,
        456,1,0,0,0,457,458,1,0,0,0,458,459,1,0,0,0,459,460,5,8,0,0,460,
        67,1,0,0,0,461,467,3,70,35,0,462,463,3,70,35,0,463,464,5,6,0,0,464,
        465,3,68,34,0,465,467,1,0,0,0,466,461,1,0,0,0,466,462,1,0,0,0,467,
        69,1,0,0,0,468,469,3,72,36,0,469,470,5,5,0,0,470,471,3,16,8,0,471,
        71,1,0,0,0,472,473,5,68,0,0,473,73,1,0,0,0,474,475,3,16,8,0,475,
        75,1,0,0,0,476,479,3,78,39,0,477,479,3,80,40,0,478,476,1,0,0,0,478,
        477,1,0,0,0,479,77,1,0,0,0,480,481,5,7,0,0,481,482,3,72,36,0,482,
        483,5,8,0,0,483,79,1,0,0,0,484,485,5,7,0,0,485,486,3,72,36,0,486,
        487,5,8,0,0,487,488,5,13,0,0,488,81,1,0,0,0,489,490,3,76,38,0,490,
        83,1,0,0,0,491,492,5,7,0,0,492,493,3,88,44,0,493,494,5,8,0,0,494,
        85,1,0,0,0,495,496,5,7,0,0,496,497,3,88,44,0,497,498,5,8,0,0,498,
        499,5,13,0,0,499,87,1,0,0,0,500,506,3,78,39,0,501,502,3,78,39,0,
        502,503,5,6,0,0,503,504,3,88,44,0,504,506,1,0,0,0,505,500,1,0,0,
        0,505,501,1,0,0,0,506,89,1,0,0,0,507,510,3,84,42,0,508,510,3,86,
        43,0,509,507,1,0,0,0,509,508,1,0,0,0,510,91,1,0,0,0,511,513,5,11,
        0,0,512,514,3,96,48,0,513,512,1,0,0,0,513,514,1,0,0,0,514,515,1,
        0,0,0,515,517,5,12,0,0,516,518,3,106,53,0,517,516,1,0,0,0,517,518,
        1,0,0,0,518,519,1,0,0,0,519,520,5,50,0,0,520,521,3,94,47,0,521,93,
        1,0,0,0,522,523,3,16,8,0,523,95,1,0,0,0,524,530,3,98,49,0,525,526,
        3,98,49,0,526,527,5,6,0,0,527,528,3,110,55,0,528,530,1,0,0,0,529,
        524,1,0,0,0,529,525,1,0,0,0,530,97,1,0,0,0,531,537,3,100,50,0,532,
        533,3,100,50,0,533,534,5,6,0,0,534,535,3,98,49,0,535,537,1,0,0,0,
        536,531,1,0,0,0,536,532,1,0,0,0,537,99,1,0,0,0,538,540,3,102,51,
        0,539,541,3,104,52,0,540,539,1,0,0,0,540,541,1,0,0,0,541,101,1,0,
        0,0,542,543,5,68,0,0,543,103,1,0,0,0,544,545,3,108,54,0,545,105,
        1,0,0,0,546,547,3,108,54,0,547,107,1,0,0,0,548,549,5,49,0,0,549,
        550,3,24,12,0,550,109,1,0,0,0,551,557,3,112,56,0,552,553,3,112,56,
        0,553,554,5,6,0,0,554,555,3,110,55,0,555,557,1,0,0,0,556,551,1,0,
        0,0,556,552,1,0,0,0,557,111,1,0,0,0,558,559,5,14,0,0,559,560,3,100,
        50,0,560,113,1,0,0,0,561,562,5,28,0,0,562,563,3,116,58,0,563,115,
        1,0,0,0,564,565,3,94,47,0,565,117,1,0,0,0,566,567,5,29,0,0,567,568,
        3,120,60,0,568,569,5,30,0,0,569,570,3,16,8,0,570,119,1,0,0,0,571,
        577,3,122,61,0,572,573,3,122,61,0,573,574,5,6,0,0,574,575,3,120,
        60,0,575,577,1,0,0,0,576,571,1,0,0,0,576,572,1,0,0,0,577,121,1,0,
        0,0,578,579,3,124,62,0,579,580,5,5,0,0,580,581,3,16,8,0,581,123,
        1,0,0,0,582,583,5,68,0,0,583,125,1,0,0,0,584,585,5,31,0,0,585,586,
        3,128,64,0,586,587,5,32,0,0,587,588,3,130,65,0,588,589,5,33,0,0,
        589,590,3,132,66,0,590,127,1,0,0,0,591,592,3,16,8,0,592,129,1,0,
        0,0,593,594,3,16,8,0,594,131,1,0,0,0,595,596,3,16,8,0,596,133,1,
        0,0,0,597,601,3,40,20,0,598,599,5,27,0,0,599,601,3,138,69,0,600,
        597,1,0,0,0,600,598,1,0,0,0,601,135,1,0,0,0,602,605,3,54,27,0,603,
        605,3,138,69,0,604,602,1,0,0,0,604,603,1,0,0,0,605,137,1,0,0,0,606,
        613,3,140,70,0,607,613,3,142,71,0,608,613,3,154,77,0,609,613,3,158,
        79,0,610,613,3,172,86,0,611,613,3,176,88,0,612,606,1,0,0,0,612,607,
        1,0,0,0,612,608,1,0,0,0,612,609,1,0,0,0,612,610,1,0,0,0,612,611,
        1,0,0,0,613,139,1,0,0,0,614,615,7,0,0,0,615,141,1,0,0,0,616,617,
        5,7,0,0,617,618,3,152,76,0,618,619,5,8,0,0,619,632,1,0,0,0,620,622,
        5,7,0,0,621,623,3,144,72,0,622,621,1,0,0,0,622,623,1,0,0,0,623,624,
        1,0,0,0,624,632,5,8,0,0,625,626,5,7,0,0,626,627,3,144,72,0,627,628,
        5,6,0,0,628,629,3,152,76,0,629,630,5,8,0,0,630,632,1,0,0,0,631,616,
        1,0,0,0,631,620,1,0,0,0,631,625,1,0,0,0,632,143,1,0,0,0,633,639,
        3,146,73,0,634,635,3,146,73,0,635,636,5,6,0,0,636,637,3,144,72,0,
        637,639,1,0,0,0,638,633,1,0,0,0,638,634,1,0,0,0,639,145,1,0,0,0,
        640,642,5,14,0,0,641,640,1,0,0,0,641,642,1,0,0,0,642,643,1,0,0,0,
        643,645,3,72,36,0,644,646,3,148,74,0,645,644,1,0,0,0,645,646,1,0,
        0,0,646,147,1,0,0,0,647,648,5,5,0,0,648,649,3,150,75,0,649,149,1,
        0,0,0,650,651,3,136,68,0,651,151,1,0,0,0,652,653,5,26,0,0,653,153,
        1,0,0,0,654,655,5,9,0,0,655,656,3,156,78,0,656,657,5,10,0,0,657,
        155,1,0,0,0,658,659,3,136,68,0,659,157,1,0,0,0,660,662,5,25,0,0,
        661,663,3,160,80,0,662,661,1,0,0,0,662,663,1,0,0,0,663,664,1,0,0,
        0,664,665,5,12,0,0,665,666,3,106,53,0,666,159,1,0,0,0,667,674,3,
        162,81,0,668,669,3,162,81,0,669,670,5,6,0,0,670,671,3,166,83,0,671,
        674,1,0,0,0,672,674,3,166,83,0,673,667,1,0,0,0,673,668,1,0,0,0,673,
        672,1,0,0,0,674,161,1,0,0,0,675,681,3,164,82,0,676,677,3,164,82,
        0,677,678,5,6,0,0,678,679,3,162,81,0,679,681,1,0,0,0,680,675,1,0,
        0,0,680,676,1,0,0,0,681,163,1,0,0,0,682,683,3,170,85,0,683,165,1,
        0,0,0,684,690,3,168,84,0,685,686,3,168,84,0,686,687,5,6,0,0,687,
        688,3,166,83,0,688,690,1,0,0,0,689,684,1,0,0,0,689,685,1,0,0,0,690,
        167,1,0,0,0,691,692,5,14,0,0,692,693,3,170,85,0,693,169,1,0,0,0,
        694,695,3,102,51,0,695,696,3,104,52,0,696,171,1,0,0,0,697,698,5,
        15,0,0,698,699,3,174,87,0,699,173,1,0,0,0,700,701,5,7,0,0,701,702,
        3,144,72,0,702,703,5,8,0,0,703,175,1,0,0,0,704,705,5,16,0,0,705,
        706,3,136,68,0,706,177,1,0,0,0,707,708,5,24,0,0,708,709,3,16,8,0,
        709,179,1,0,0,0,710,711,5,23,0,0,711,713,3,182,91,0,712,714,3,184,
        92,0,713,712,1,0,0,0,713,714,1,0,0,0,714,181,1,0,0,0,715,716,3,16,
        8,0,716,183,1,0,0,0,717,718,5,22,0,0,718,719,3,186,93,0,719,185,
        1,0,0,0,720,721,3,16,8,0,721,187,1,0,0,0,722,723,3,190,95,0,723,
        189,1,0,0,0,724,726,5,7,0,0,725,727,3,192,96,0,726,725,1,0,0,0,726,
        727,1,0,0,0,727,728,1,0,0,0,728,729,5,8,0,0,729,191,1,0,0,0,730,
        736,3,194,97,0,731,732,3,194,97,0,732,733,5,6,0,0,733,734,3,192,
        96,0,734,736,1,0,0,0,735,730,1,0,0,0,735,731,1,0,0,0,736,193,1,0,
        0,0,737,738,3,72,36,0,738,739,5,5,0,0,739,740,3,200,100,0,740,195,
        1,0,0,0,741,743,5,9,0,0,742,744,3,198,99,0,743,742,1,0,0,0,743,744,
        1,0,0,0,744,745,1,0,0,0,745,746,5,10,0,0,746,197,1,0,0,0,747,753,
        3,200,100,0,748,749,3,200,100,0,749,750,5,6,0,0,750,751,3,198,99,
        0,751,753,1,0,0,0,752,747,1,0,0,0,752,748,1,0,0,0,753,199,1,0,0,
        0,754,758,3,190,95,0,755,758,3,196,98,0,756,758,5,66,0,0,757,754,
        1,0,0,0,757,755,1,0,0,0,757,756,1,0,0,0,758,201,1,0,0,0,57,204,209,
        215,221,224,227,246,253,263,274,278,290,302,321,336,347,354,363,
        375,397,400,402,411,433,437,446,453,457,466,478,505,509,513,517,
        529,536,540,556,576,600,604,612,622,631,638,641,645,662,673,680,
        689,713,726,735,743,752,757
    ]

class PowerQueryParser ( Parser ):

    grammarFileName = "PowerQueryParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "','", "'['", "']'", "'{'", "'}'", 
                     "'('", "')'", "'?'", "'optional'", "'table'", "'nullable'", 
                     "';'", "'section'", "'shared'", "'and'", "'or'", "'otherwise'", 
                     "'try'", "'error'", "'function ('", "'...'", "'type'", 
                     "'each'", "'let'", "'in'", "'if'", "'then'", "'else'", 
                     "'text'", "'record'", "'number'", "'none'", "'logical'", 
                     "'list'", "'fuction'", "'duration'", "'datetimezone'", 
                     "'any'", "'anynonnull'", "'binary'", "'date'", "'datetime'", 
                     "'@'", "'as'", "'=>'", "'..'", "'!'", "'not'", "'+'", 
                     "'-'", "'meta'", "'is'", "'<>'", "'>'", "'<'", "'/'", 
                     "'*'", "'&'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "NEW_LINE_CHAR", "COMMENT", 
                      "CHARACHTER_ESCAPE_SEQUENCE", "EQUALS", "COMMA", "OPEN_BRACKET", 
                      "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", "OPEN_PAREN", 
                      "CLOSE_PAREN", "OPTIONAL", "OPTIONAL_TEXT", "TABLE", 
                      "NULLABLE", "SEMICOLON", "SECTION", "SHARED", "AND", 
                      "OR", "OTHERWISE", "TRY", "ERROR", "FUNCTION_START", 
                      "ELLIPSES", "TYPE", "EACH", "LET", "IN", "IF", "THEN", 
                      "ELSE", "TEXT", "RECORD", "NUMBER", "NONE", "LOGICAL", 
                      "LIST", "FUNCTION", "DURATION", "DATETIMEZONE", "ANY", 
                      "ANYNONNULL", "BINARY", "DATE", "DATETIME", "AT", 
                      "AS", "ARROW", "DOTDOT", "BANG", "NOT", "PLUS", "MINUS", 
                      "META", "IS", "NEQ", "GE", "LE", "SLASH", "STAR", 
                      "AMP", "LEQ", "GEQ", "LITERAL", "TEXT_LITERAL", "IDENTIFIER", 
                      "REGULAR_IDENTIFIER", "AVAILABLE_IDENTIFIER", "KEYWORD_OR_IDENTIFIER" ]

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
    RULE_literal_expression = 21
    RULE_identifier_expression = 22
    RULE_identifier_reference = 23
    RULE_exclusive_identifier_reference = 24
    RULE_inclusive_identifier_reference = 25
    RULE_section_access_expression = 26
    RULE_parenthesized_expression = 27
    RULE_not_implemented_expression = 28
    RULE_argument_list = 29
    RULE_list_expression = 30
    RULE_item_list = 31
    RULE_item = 32
    RULE_record_expression = 33
    RULE_field_list = 34
    RULE_field = 35
    RULE_field_name = 36
    RULE_item_selector = 37
    RULE_field_selector = 38
    RULE_required_field_selector = 39
    RULE_optional_field_selector = 40
    RULE_implicit_target_field_selection = 41
    RULE_required_projection = 42
    RULE_optional_projection = 43
    RULE_required_selector_list = 44
    RULE_implicit_target_projection = 45
    RULE_function_expression = 46
    RULE_function_body = 47
    RULE_parameter_list = 48
    RULE_fixed_parameter_list = 49
    RULE_parameter = 50
    RULE_parameter_name = 51
    RULE_parameter_type = 52
    RULE_return_type = 53
    RULE_assertion = 54
    RULE_optional_parameter_list = 55
    RULE_optional_parameter = 56
    RULE_each_expression = 57
    RULE_each_expression_body = 58
    RULE_let_expression = 59
    RULE_variable_list = 60
    RULE_variable = 61
    RULE_variable_name = 62
    RULE_if_expression = 63
    RULE_if_condition = 64
    RULE_true_expression = 65
    RULE_false_expression = 66
    RULE_type_expression = 67
    RULE_type_expr = 68
    RULE_primary_type = 69
    RULE_primitive_type = 70
    RULE_record_type = 71
    RULE_field_specification_list = 72
    RULE_field_specification = 73
    RULE_field_type_specification = 74
    RULE_field_type = 75
    RULE_open_record_marker = 76
    RULE_list_type = 77
    RULE_item_type = 78
    RULE_function_type = 79
    RULE_parameter_specification_list = 80
    RULE_required_parameter_specification_list = 81
    RULE_required_parameter_specification = 82
    RULE_optional_parameter_specification_list = 83
    RULE_optional_parameter_specification = 84
    RULE_parameter_specification = 85
    RULE_table_type = 86
    RULE_row_type = 87
    RULE_nullable_type = 88
    RULE_error_raising_expression = 89
    RULE_error_handling_expression = 90
    RULE_protected_expression = 91
    RULE_otherwise_clause = 92
    RULE_default_expression = 93
    RULE_literal_attribs = 94
    RULE_record_literal = 95
    RULE_literal_field_list = 96
    RULE_literal_field = 97
    RULE_list_literal = 98
    RULE_literal_item_list = 99
    RULE_any_literal = 100

    ruleNames =  [ "document", "section_document", "section", "section_name", 
                   "section_members", "section_member", "section_member_name", 
                   "expression_document", "expression", "logical_or_expression", 
                   "logical_and_expression", "is_expression", "nullable_primitive_type", 
                   "as_expression", "equality_expression", "relational_expression", 
                   "additive_expression", "multiplicative_expression", "metadata_expression", 
                   "unary_expression", "primary_expression", "literal_expression", 
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
    COMMENT=3
    CHARACHTER_ESCAPE_SEQUENCE=4
    EQUALS=5
    COMMA=6
    OPEN_BRACKET=7
    CLOSE_BRACKET=8
    OPEN_BRACE=9
    CLOSE_BRACE=10
    OPEN_PAREN=11
    CLOSE_PAREN=12
    OPTIONAL=13
    OPTIONAL_TEXT=14
    TABLE=15
    NULLABLE=16
    SEMICOLON=17
    SECTION=18
    SHARED=19
    AND=20
    OR=21
    OTHERWISE=22
    TRY=23
    ERROR=24
    FUNCTION_START=25
    ELLIPSES=26
    TYPE=27
    EACH=28
    LET=29
    IN=30
    IF=31
    THEN=32
    ELSE=33
    TEXT=34
    RECORD=35
    NUMBER=36
    NONE=37
    LOGICAL=38
    LIST=39
    FUNCTION=40
    DURATION=41
    DATETIMEZONE=42
    ANY=43
    ANYNONNULL=44
    BINARY=45
    DATE=46
    DATETIME=47
    AT=48
    AS=49
    ARROW=50
    DOTDOT=51
    BANG=52
    NOT=53
    PLUS=54
    MINUS=55
    META=56
    IS=57
    NEQ=58
    GE=59
    LE=60
    SLASH=61
    STAR=62
    AMP=63
    LEQ=64
    GEQ=65
    LITERAL=66
    TEXT_LITERAL=67
    IDENTIFIER=68
    REGULAR_IDENTIFIER=69
    AVAILABLE_IDENTIFIER=70
    KEYWORD_OR_IDENTIFIER=71

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
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
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.section_document()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
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
            self.state = 206
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
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.OPEN_BRACKET:
                self.state = 208
                self.literal_attribs()


            self.state = 211
            self.match(PowerQueryParser.SECTION)
            self.state = 212
            self.section_name()
            self.state = 213
            self.match(PowerQueryParser.SEMICOLON)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (PowerQueryParser.OPEN_BRACKET - 7)) | (1 << (PowerQueryParser.SHARED - 7)) | (1 << (PowerQueryParser.IDENTIFIER - 7)))) != 0):
                self.state = 214
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
            self.state = 217
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
            self.state = 219
            self.section_member()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (PowerQueryParser.OPEN_BRACKET - 7)) | (1 << (PowerQueryParser.SHARED - 7)) | (1 << (PowerQueryParser.IDENTIFIER - 7)))) != 0):
                self.state = 220
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
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.OPEN_BRACKET:
                self.state = 223
                self.literal_attribs()


            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.SHARED:
                self.state = 226
                self.match(PowerQueryParser.SHARED)


            self.state = 229
            self.section_member_name()
            self.state = 230
            self.match(PowerQueryParser.EQUALS)
            self.state = 231
            self.expression()
            self.state = 232
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
            self.state = 234
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
            self.state = 236
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

        def logical_or_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Logical_or_expressionContext,0)


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
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.logical_or_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.each_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.function_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 241
                self.let_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 242
                self.if_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 243
                self.let_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 244
                self.error_raising_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 245
                self.error_handling_expression()
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

        def logical_and_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Logical_and_expressionContext,0)


        def OR(self):
            return self.getToken(PowerQueryParser.OR, 0)

        def logical_or_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Logical_or_expressionContext,0)


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
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.logical_and_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.logical_and_expression(0)
                self.state = 250
                self.match(PowerQueryParser.OR)
                self.state = 251
                self.logical_or_expression()
                pass


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

        def is_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Is_expressionContext,0)


        def logical_and_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Logical_and_expressionContext,0)


        def AND(self):
            return self.getToken(PowerQueryParser.AND, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_logical_and_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_and_expression" ):
                listener.enterLogical_and_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_and_expression" ):
                listener.exitLogical_and_expression(self)



    def logical_and_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PowerQueryParser.Logical_and_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_logical_and_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.is_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PowerQueryParser.Logical_and_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_and_expression)
                    self.state = 258
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 259
                    self.match(PowerQueryParser.AND)
                    self.state = 260
                    self.is_expression(0) 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Is_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def as_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.As_expressionContext,0)


        def is_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Is_expressionContext,0)


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



    def is_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PowerQueryParser.Is_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_is_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.as_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PowerQueryParser.Is_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_is_expression)
                    self.state = 269
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 270
                    self.match(PowerQueryParser.IS)
                    self.state = 271
                    self.nullable_primitive_type() 
                self.state = 276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.NULLABLE:
                self.state = 277
                self.match(PowerQueryParser.NULLABLE)


            self.state = 280
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


        def as_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.As_expressionContext,0)


        def AS(self):
            return self.getToken(PowerQueryParser.AS, 0)

        def nullable_primitive_type(self):
            return self.getTypedRuleContext(PowerQueryParser.Nullable_primitive_typeContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_as_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAs_expression" ):
                listener.enterAs_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAs_expression" ):
                listener.exitAs_expression(self)



    def as_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PowerQueryParser.As_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_as_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.equality_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PowerQueryParser.As_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_as_expression)
                    self.state = 285
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 286
                    self.match(PowerQueryParser.AS)
                    self.state = 287
                    self.nullable_primitive_type() 
                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Equality_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Relational_expressionContext,0)


        def EQUALS(self):
            return self.getToken(PowerQueryParser.EQUALS, 0)

        def equality_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Equality_expressionContext,0)


        def NEQ(self):
            return self.getToken(PowerQueryParser.NEQ, 0)

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
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.relational_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.relational_expression()
                self.state = 295
                self.match(PowerQueryParser.EQUALS)
                self.state = 296
                self.equality_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.relational_expression()
                self.state = 299
                self.match(PowerQueryParser.NEQ)
                self.state = 300
                self.equality_expression()
                pass


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


        def LE(self):
            return self.getToken(PowerQueryParser.LE, 0)

        def relational_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Relational_expressionContext,0)


        def GE(self):
            return self.getToken(PowerQueryParser.GE, 0)

        def LEQ(self):
            return self.getToken(PowerQueryParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(PowerQueryParser.GEQ, 0)

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
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.additive_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.additive_expression()
                self.state = 306
                self.match(PowerQueryParser.LE)
                self.state = 307
                self.relational_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                self.additive_expression()
                self.state = 310
                self.match(PowerQueryParser.GE)
                self.state = 311
                self.relational_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.additive_expression()
                self.state = 314
                self.match(PowerQueryParser.LEQ)
                self.state = 315
                self.additive_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 317
                self.additive_expression()
                self.state = 318
                self.match(PowerQueryParser.GEQ)
                self.state = 319
                self.relational_expression()
                pass


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

        def multiplicative_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Multiplicative_expressionContext,0)


        def PLUS(self):
            return self.getToken(PowerQueryParser.PLUS, 0)

        def additive_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Additive_expressionContext,0)


        def MINUS(self):
            return self.getToken(PowerQueryParser.MINUS, 0)

        def AMP(self):
            return self.getToken(PowerQueryParser.AMP, 0)

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
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.multiplicative_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.multiplicative_expression()
                self.state = 325
                self.match(PowerQueryParser.PLUS)
                self.state = 326
                self.additive_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.multiplicative_expression()
                self.state = 329
                self.match(PowerQueryParser.MINUS)
                self.state = 330
                self.additive_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 332
                self.multiplicative_expression()
                self.state = 333
                self.match(PowerQueryParser.AMP)
                self.state = 334
                self.additive_expression()
                pass


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

        def metadata_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Metadata_expressionContext,0)


        def STAR(self):
            return self.getToken(PowerQueryParser.STAR, 0)

        def multiplicative_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Multiplicative_expressionContext,0)


        def SLASH(self):
            return self.getToken(PowerQueryParser.SLASH, 0)

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
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.metadata_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.metadata_expression()
                self.state = 340
                self.match(PowerQueryParser.STAR)
                self.state = 341
                self.multiplicative_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.metadata_expression()
                self.state = 344
                self.match(PowerQueryParser.SLASH)
                self.state = 345
                self.multiplicative_expression()
                pass


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


        def META(self):
            return self.getToken(PowerQueryParser.META, 0)

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
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.unary_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.unary_expression()
                self.state = 351
                self.match(PowerQueryParser.META)
                self.state = 352
                self.unary_expression()
                pass


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

        def type_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Type_expressionContext,0)


        def PLUS(self):
            return self.getToken(PowerQueryParser.PLUS, 0)

        def unary_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Unary_expressionContext,0)


        def MINUS(self):
            return self.getToken(PowerQueryParser.MINUS, 0)

        def NOT(self):
            return self.getToken(PowerQueryParser.NOT, 0)

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
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PowerQueryParser.OPEN_BRACKET, PowerQueryParser.OPEN_BRACE, PowerQueryParser.OPEN_PAREN, PowerQueryParser.ELLIPSES, PowerQueryParser.TYPE, PowerQueryParser.AT, PowerQueryParser.LITERAL, PowerQueryParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.type_expression()
                pass
            elif token in [PowerQueryParser.PLUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.match(PowerQueryParser.PLUS)
                self.state = 358
                self.unary_expression()
                pass
            elif token in [PowerQueryParser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 359
                self.match(PowerQueryParser.MINUS)
                self.state = 360
                self.unary_expression()
                pass
            elif token in [PowerQueryParser.NOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 361
                self.match(PowerQueryParser.NOT)
                self.state = 362
                self.unary_expression()
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


        def implicit_target_field_selection(self):
            return self.getTypedRuleContext(PowerQueryParser.Implicit_target_field_selectionContext,0)


        def implicit_target_projection(self):
            return self.getTypedRuleContext(PowerQueryParser.Implicit_target_projectionContext,0)


        def not_implemented_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Not_implemented_expressionContext,0)


        def primary_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Primary_expressionContext,0)


        def field_selector(self):
            return self.getTypedRuleContext(PowerQueryParser.Field_selectorContext,0)


        def required_projection(self):
            return self.getTypedRuleContext(PowerQueryParser.Required_projectionContext,0)


        def optional_projection(self):
            return self.getTypedRuleContext(PowerQueryParser.Optional_projectionContext,0)


        def OPEN_BRACE(self):
            return self.getToken(PowerQueryParser.OPEN_BRACE, 0)

        def item_selector(self):
            return self.getTypedRuleContext(PowerQueryParser.Item_selectorContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACE, 0)

        def OPTIONAL(self):
            return self.getToken(PowerQueryParser.OPTIONAL, 0)

        def OPEN_PAREN(self):
            return self.getToken(PowerQueryParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(PowerQueryParser.CLOSE_PAREN, 0)

        def argument_list(self):
            return self.getTypedRuleContext(PowerQueryParser.Argument_listContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_primary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression" ):
                listener.enterPrimary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression" ):
                listener.exitPrimary_expression(self)



    def primary_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PowerQueryParser.Primary_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_primary_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 366
                self.literal_expression()
                pass

            elif la_ == 2:
                self.state = 367
                self.list_expression()
                pass

            elif la_ == 3:
                self.state = 368
                self.record_expression()
                pass

            elif la_ == 4:
                self.state = 369
                self.identifier_expression()
                pass

            elif la_ == 5:
                self.state = 370
                self.section_access_expression()
                pass

            elif la_ == 6:
                self.state = 371
                self.parenthesized_expression()
                pass

            elif la_ == 7:
                self.state = 372
                self.implicit_target_field_selection()
                pass

            elif la_ == 8:
                self.state = 373
                self.implicit_target_projection()
                pass

            elif la_ == 9:
                self.state = 374
                self.not_implemented_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 400
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = PowerQueryParser.Primary_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expression)
                        self.state = 377
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 378
                        self.field_selector()
                        pass

                    elif la_ == 2:
                        localctx = PowerQueryParser.Primary_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expression)
                        self.state = 379
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 380
                        self.required_projection()
                        pass

                    elif la_ == 3:
                        localctx = PowerQueryParser.Primary_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expression)
                        self.state = 381
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 382
                        self.optional_projection()
                        pass

                    elif la_ == 4:
                        localctx = PowerQueryParser.Primary_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expression)
                        self.state = 383
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 384
                        self.match(PowerQueryParser.OPEN_BRACE)
                        self.state = 385
                        self.item_selector()
                        self.state = 386
                        self.match(PowerQueryParser.CLOSE_BRACE)
                        pass

                    elif la_ == 5:
                        localctx = PowerQueryParser.Primary_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expression)
                        self.state = 388
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 389
                        self.match(PowerQueryParser.OPEN_BRACE)
                        self.state = 390
                        self.item_selector()
                        self.state = 391
                        self.match(PowerQueryParser.CLOSE_BRACE)
                        self.state = 392
                        self.match(PowerQueryParser.OPTIONAL)
                        pass

                    elif la_ == 6:
                        localctx = PowerQueryParser.Primary_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expression)
                        self.state = 394
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 395
                        self.match(PowerQueryParser.OPEN_PAREN)
                        self.state = 397
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (PowerQueryParser.OPEN_BRACKET - 7)) | (1 << (PowerQueryParser.OPEN_BRACE - 7)) | (1 << (PowerQueryParser.OPEN_PAREN - 7)) | (1 << (PowerQueryParser.TRY - 7)) | (1 << (PowerQueryParser.ERROR - 7)) | (1 << (PowerQueryParser.ELLIPSES - 7)) | (1 << (PowerQueryParser.TYPE - 7)) | (1 << (PowerQueryParser.EACH - 7)) | (1 << (PowerQueryParser.LET - 7)) | (1 << (PowerQueryParser.IF - 7)) | (1 << (PowerQueryParser.AT - 7)) | (1 << (PowerQueryParser.NOT - 7)) | (1 << (PowerQueryParser.PLUS - 7)) | (1 << (PowerQueryParser.MINUS - 7)) | (1 << (PowerQueryParser.LITERAL - 7)) | (1 << (PowerQueryParser.IDENTIFIER - 7)))) != 0):
                            self.state = 396
                            self.argument_list()


                        self.state = 399
                        self.match(PowerQueryParser.CLOSE_PAREN)
                        pass

             
                self.state = 404
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 42, self.RULE_literal_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
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
        self.enterRule(localctx, 44, self.RULE_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
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
        self.enterRule(localctx, 46, self.RULE_identifier_reference)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PowerQueryParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.exclusive_identifier_reference()
                pass
            elif token in [PowerQueryParser.AT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
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
        self.enterRule(localctx, 48, self.RULE_exclusive_identifier_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
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
        self.enterRule(localctx, 50, self.RULE_inclusive_identifier_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(PowerQueryParser.AT)
            self.state = 416
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
        self.enterRule(localctx, 52, self.RULE_section_access_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(PowerQueryParser.IDENTIFIER)
            self.state = 419
            self.match(PowerQueryParser.BANG)
            self.state = 420
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
        self.enterRule(localctx, 54, self.RULE_parenthesized_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(PowerQueryParser.OPEN_PAREN)
            self.state = 423
            self.expression()
            self.state = 424
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
        self.enterRule(localctx, 56, self.RULE_not_implemented_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
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
        self.enterRule(localctx, 58, self.RULE_argument_list)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.expression()
                self.state = 430
                self.match(PowerQueryParser.COMMA)
                self.state = 431
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
        self.enterRule(localctx, 60, self.RULE_list_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(PowerQueryParser.OPEN_BRACE)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (PowerQueryParser.OPEN_BRACKET - 7)) | (1 << (PowerQueryParser.OPEN_BRACE - 7)) | (1 << (PowerQueryParser.OPEN_PAREN - 7)) | (1 << (PowerQueryParser.TRY - 7)) | (1 << (PowerQueryParser.ERROR - 7)) | (1 << (PowerQueryParser.ELLIPSES - 7)) | (1 << (PowerQueryParser.TYPE - 7)) | (1 << (PowerQueryParser.EACH - 7)) | (1 << (PowerQueryParser.LET - 7)) | (1 << (PowerQueryParser.IF - 7)) | (1 << (PowerQueryParser.AT - 7)) | (1 << (PowerQueryParser.NOT - 7)) | (1 << (PowerQueryParser.PLUS - 7)) | (1 << (PowerQueryParser.MINUS - 7)) | (1 << (PowerQueryParser.LITERAL - 7)) | (1 << (PowerQueryParser.IDENTIFIER - 7)))) != 0):
                self.state = 436
                self.item_list()


            self.state = 439
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
        self.enterRule(localctx, 62, self.RULE_item_list)
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.item()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.item()
                self.state = 443
                self.match(PowerQueryParser.COMMA)
                self.state = 444
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
        self.enterRule(localctx, 64, self.RULE_item)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.expression()
                self.state = 450
                self.match(PowerQueryParser.DOTDOT)
                self.state = 451
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
        self.enterRule(localctx, 66, self.RULE_record_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.IDENTIFIER:
                self.state = 456
                self.field_list()


            self.state = 459
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
        self.enterRule(localctx, 68, self.RULE_field_list)
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.field()
                self.state = 463
                self.match(PowerQueryParser.COMMA)
                self.state = 464
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
        self.enterRule(localctx, 70, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.field_name()
            self.state = 469
            self.match(PowerQueryParser.EQUALS)
            self.state = 470
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
        self.enterRule(localctx, 72, self.RULE_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
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
        self.enterRule(localctx, 74, self.RULE_item_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
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
        self.enterRule(localctx, 76, self.RULE_field_selector)
        try:
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 476
                self.required_field_selector()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 477
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
        self.enterRule(localctx, 78, self.RULE_required_field_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 481
            self.field_name()
            self.state = 482
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
        self.enterRule(localctx, 80, self.RULE_optional_field_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 485
            self.field_name()
            self.state = 486
            self.match(PowerQueryParser.CLOSE_BRACKET)
            self.state = 487
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
        self.enterRule(localctx, 82, self.RULE_implicit_target_field_selection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
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
        self.enterRule(localctx, 84, self.RULE_required_projection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 492
            self.required_selector_list()
            self.state = 493
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
        self.enterRule(localctx, 86, self.RULE_optional_projection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 496
            self.required_selector_list()
            self.state = 497
            self.match(PowerQueryParser.CLOSE_BRACKET)
            self.state = 498
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
        self.enterRule(localctx, 88, self.RULE_required_selector_list)
        try:
            self.state = 505
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.required_field_selector()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.required_field_selector()
                self.state = 502
                self.match(PowerQueryParser.COMMA)
                self.state = 503
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
        self.enterRule(localctx, 90, self.RULE_implicit_target_projection)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.required_projection()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
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
        self.enterRule(localctx, 92, self.RULE_function_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(PowerQueryParser.OPEN_PAREN)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.IDENTIFIER:
                self.state = 512
                self.parameter_list()


            self.state = 515
            self.match(PowerQueryParser.CLOSE_PAREN)
            self.state = 517
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.AS:
                self.state = 516
                self.return_type()


            self.state = 519
            self.match(PowerQueryParser.ARROW)
            self.state = 520
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
        self.enterRule(localctx, 94, self.RULE_function_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
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
        self.enterRule(localctx, 96, self.RULE_parameter_list)
        try:
            self.state = 529
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.fixed_parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.fixed_parameter_list()
                self.state = 526
                self.match(PowerQueryParser.COMMA)
                self.state = 527
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
        self.enterRule(localctx, 98, self.RULE_fixed_parameter_list)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.parameter()
                self.state = 533
                self.match(PowerQueryParser.COMMA)
                self.state = 534
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
        self.enterRule(localctx, 100, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.parameter_name()
            self.state = 540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.AS:
                self.state = 539
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
        self.enterRule(localctx, 102, self.RULE_parameter_name)
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
        self.enterRule(localctx, 104, self.RULE_parameter_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
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
        self.enterRule(localctx, 106, self.RULE_return_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
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
        self.enterRule(localctx, 108, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(PowerQueryParser.AS)
            self.state = 549
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
        self.enterRule(localctx, 110, self.RULE_optional_parameter_list)
        try:
            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.optional_parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.optional_parameter()
                self.state = 553
                self.match(PowerQueryParser.COMMA)
                self.state = 554
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
        self.enterRule(localctx, 112, self.RULE_optional_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(PowerQueryParser.OPTIONAL_TEXT)
            self.state = 559
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
        self.enterRule(localctx, 114, self.RULE_each_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(PowerQueryParser.EACH)
            self.state = 562
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
        self.enterRule(localctx, 116, self.RULE_each_expression_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
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
        self.enterRule(localctx, 118, self.RULE_let_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.match(PowerQueryParser.LET)
            self.state = 567
            self.variable_list()
            self.state = 568
            self.match(PowerQueryParser.IN)
            self.state = 569
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
        self.enterRule(localctx, 120, self.RULE_variable_list)
        try:
            self.state = 576
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 571
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 572
                self.variable()
                self.state = 573
                self.match(PowerQueryParser.COMMA)
                self.state = 574
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
        self.enterRule(localctx, 122, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self.variable_name()
            self.state = 579
            self.match(PowerQueryParser.EQUALS)
            self.state = 580
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
        self.enterRule(localctx, 124, self.RULE_variable_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
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
        self.enterRule(localctx, 126, self.RULE_if_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.match(PowerQueryParser.IF)
            self.state = 585
            self.if_condition()
            self.state = 586
            self.match(PowerQueryParser.THEN)
            self.state = 587
            self.true_expression()
            self.state = 588
            self.match(PowerQueryParser.ELSE)
            self.state = 589
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
        self.enterRule(localctx, 128, self.RULE_if_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
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
        self.enterRule(localctx, 130, self.RULE_true_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
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
        self.enterRule(localctx, 132, self.RULE_false_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
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
        self.enterRule(localctx, 134, self.RULE_type_expression)
        try:
            self.state = 600
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PowerQueryParser.OPEN_BRACKET, PowerQueryParser.OPEN_BRACE, PowerQueryParser.OPEN_PAREN, PowerQueryParser.ELLIPSES, PowerQueryParser.AT, PowerQueryParser.LITERAL, PowerQueryParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 597
                self.primary_expression(0)
                pass
            elif token in [PowerQueryParser.TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 598
                self.match(PowerQueryParser.TYPE)
                self.state = 599
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
        self.enterRule(localctx, 136, self.RULE_type_expr)
        try:
            self.state = 604
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PowerQueryParser.OPEN_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 602
                self.parenthesized_expression()
                pass
            elif token in [PowerQueryParser.OPEN_BRACKET, PowerQueryParser.OPEN_BRACE, PowerQueryParser.TABLE, PowerQueryParser.NULLABLE, PowerQueryParser.FUNCTION_START, PowerQueryParser.TYPE, PowerQueryParser.TEXT, PowerQueryParser.RECORD, PowerQueryParser.NUMBER, PowerQueryParser.NONE, PowerQueryParser.LOGICAL, PowerQueryParser.LIST, PowerQueryParser.FUNCTION, PowerQueryParser.DURATION, PowerQueryParser.DATETIMEZONE, PowerQueryParser.ANY, PowerQueryParser.ANYNONNULL, PowerQueryParser.BINARY, PowerQueryParser.DATE, PowerQueryParser.DATETIME, PowerQueryParser.LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 603
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
        self.enterRule(localctx, 138, self.RULE_primary_type)
        try:
            self.state = 612
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 606
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 607
                self.record_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 608
                self.list_type()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 609
                self.function_type()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 610
                self.table_type()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 611
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
        self.enterRule(localctx, 140, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            _la = self._input.LA(1)
            if not(((((_la - 15)) & ~0x3f) == 0 and ((1 << (_la - 15)) & ((1 << (PowerQueryParser.TABLE - 15)) | (1 << (PowerQueryParser.TYPE - 15)) | (1 << (PowerQueryParser.TEXT - 15)) | (1 << (PowerQueryParser.RECORD - 15)) | (1 << (PowerQueryParser.NUMBER - 15)) | (1 << (PowerQueryParser.NONE - 15)) | (1 << (PowerQueryParser.LOGICAL - 15)) | (1 << (PowerQueryParser.LIST - 15)) | (1 << (PowerQueryParser.FUNCTION - 15)) | (1 << (PowerQueryParser.DURATION - 15)) | (1 << (PowerQueryParser.DATETIMEZONE - 15)) | (1 << (PowerQueryParser.ANY - 15)) | (1 << (PowerQueryParser.ANYNONNULL - 15)) | (1 << (PowerQueryParser.BINARY - 15)) | (1 << (PowerQueryParser.DATE - 15)) | (1 << (PowerQueryParser.DATETIME - 15)) | (1 << (PowerQueryParser.LITERAL - 15)))) != 0)):
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
        self.enterRule(localctx, 142, self.RULE_record_type)
        self._la = 0 # Token type
        try:
            self.state = 631
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 616
                self.match(PowerQueryParser.OPEN_BRACKET)
                self.state = 617
                self.open_record_marker()
                self.state = 618
                self.match(PowerQueryParser.CLOSE_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 620
                self.match(PowerQueryParser.OPEN_BRACKET)
                self.state = 622
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PowerQueryParser.OPTIONAL_TEXT or _la==PowerQueryParser.IDENTIFIER:
                    self.state = 621
                    self.field_specification_list()


                self.state = 624
                self.match(PowerQueryParser.CLOSE_BRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 625
                self.match(PowerQueryParser.OPEN_BRACKET)
                self.state = 626
                self.field_specification_list()
                self.state = 627
                self.match(PowerQueryParser.COMMA)
                self.state = 628
                self.open_record_marker()
                self.state = 629
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
        self.enterRule(localctx, 144, self.RULE_field_specification_list)
        try:
            self.state = 638
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 633
                self.field_specification()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 634
                self.field_specification()
                self.state = 635
                self.match(PowerQueryParser.COMMA)
                self.state = 636
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
        self.enterRule(localctx, 146, self.RULE_field_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.OPTIONAL_TEXT:
                self.state = 640
                self.match(PowerQueryParser.OPTIONAL_TEXT)


            self.state = 643
            self.field_name()
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.EQUALS:
                self.state = 644
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
        self.enterRule(localctx, 148, self.RULE_field_type_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.match(PowerQueryParser.EQUALS)
            self.state = 648
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
        self.enterRule(localctx, 150, self.RULE_field_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
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
        self.enterRule(localctx, 152, self.RULE_open_record_marker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
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
        self.enterRule(localctx, 154, self.RULE_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.match(PowerQueryParser.OPEN_BRACE)
            self.state = 655
            self.item_type()
            self.state = 656
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
        self.enterRule(localctx, 156, self.RULE_item_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
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
        self.enterRule(localctx, 158, self.RULE_function_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            self.match(PowerQueryParser.FUNCTION_START)
            self.state = 662
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.OPTIONAL_TEXT or _la==PowerQueryParser.IDENTIFIER:
                self.state = 661
                self.parameter_specification_list()


            self.state = 664
            self.match(PowerQueryParser.CLOSE_PAREN)
            self.state = 665
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
        self.enterRule(localctx, 160, self.RULE_parameter_specification_list)
        try:
            self.state = 673
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 667
                self.required_parameter_specification_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 668
                self.required_parameter_specification_list()
                self.state = 669
                self.match(PowerQueryParser.COMMA)
                self.state = 670
                self.optional_parameter_specification_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 672
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
        self.enterRule(localctx, 162, self.RULE_required_parameter_specification_list)
        try:
            self.state = 680
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 675
                self.required_parameter_specification()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 676
                self.required_parameter_specification()
                self.state = 677
                self.match(PowerQueryParser.COMMA)
                self.state = 678
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
        self.enterRule(localctx, 164, self.RULE_required_parameter_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
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
        self.enterRule(localctx, 166, self.RULE_optional_parameter_specification_list)
        try:
            self.state = 689
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 684
                self.optional_parameter_specification()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 685
                self.optional_parameter_specification()
                self.state = 686
                self.match(PowerQueryParser.COMMA)
                self.state = 687
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
        self.enterRule(localctx, 168, self.RULE_optional_parameter_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 691
            self.match(PowerQueryParser.OPTIONAL_TEXT)
            self.state = 692
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
        self.enterRule(localctx, 170, self.RULE_parameter_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 694
            self.parameter_name()
            self.state = 695
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
        self.enterRule(localctx, 172, self.RULE_table_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 697
            self.match(PowerQueryParser.TABLE)
            self.state = 698
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
        self.enterRule(localctx, 174, self.RULE_row_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 700
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 701
            self.field_specification_list()
            self.state = 702
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
        self.enterRule(localctx, 176, self.RULE_nullable_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 704
            self.match(PowerQueryParser.NULLABLE)
            self.state = 705
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
        self.enterRule(localctx, 178, self.RULE_error_raising_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 707
            self.match(PowerQueryParser.ERROR)
            self.state = 708
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
        self.enterRule(localctx, 180, self.RULE_error_handling_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 710
            self.match(PowerQueryParser.TRY)
            self.state = 711
            self.protected_expression()
            self.state = 713
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 712
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
        self.enterRule(localctx, 182, self.RULE_protected_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 715
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
        self.enterRule(localctx, 184, self.RULE_otherwise_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717
            self.match(PowerQueryParser.OTHERWISE)
            self.state = 718
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
        self.enterRule(localctx, 186, self.RULE_default_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
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
        self.enterRule(localctx, 188, self.RULE_literal_attribs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
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
        self.enterRule(localctx, 190, self.RULE_record_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 724
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 726
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PowerQueryParser.IDENTIFIER:
                self.state = 725
                self.literal_field_list()


            self.state = 728
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
        self.enterRule(localctx, 192, self.RULE_literal_field_list)
        try:
            self.state = 735
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 730
                self.literal_field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 731
                self.literal_field()
                self.state = 732
                self.match(PowerQueryParser.COMMA)
                self.state = 733
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
        self.enterRule(localctx, 194, self.RULE_literal_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 737
            self.field_name()
            self.state = 738
            self.match(PowerQueryParser.EQUALS)
            self.state = 739
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
        self.enterRule(localctx, 196, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            self.match(PowerQueryParser.OPEN_BRACE)
            self.state = 743
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (PowerQueryParser.OPEN_BRACKET - 7)) | (1 << (PowerQueryParser.OPEN_BRACE - 7)) | (1 << (PowerQueryParser.LITERAL - 7)))) != 0):
                self.state = 742
                self.literal_item_list()


            self.state = 745
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
        self.enterRule(localctx, 198, self.RULE_literal_item_list)
        try:
            self.state = 752
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 747
                self.any_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 748
                self.any_literal()
                self.state = 749
                self.match(PowerQueryParser.COMMA)
                self.state = 750
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
        self.enterRule(localctx, 200, self.RULE_any_literal)
        try:
            self.state = 757
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PowerQueryParser.OPEN_BRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 754
                self.record_literal()
                pass
            elif token in [PowerQueryParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 755
                self.list_literal()
                pass
            elif token in [PowerQueryParser.LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 756
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.logical_and_expression_sempred
        self._predicates[11] = self.is_expression_sempred
        self._predicates[13] = self.as_expression_sempred
        self._predicates[20] = self.primary_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_and_expression_sempred(self, localctx:Logical_and_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx:Is_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def as_expression_sempred(self, localctx:As_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def primary_expression_sempred(self, localctx:Primary_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




