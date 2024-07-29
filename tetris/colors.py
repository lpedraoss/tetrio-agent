
import numpy as np 

tetris_colors = {
#principals colors
(0,0,0):"board",
  (255,255,255):"board",
    (0,255,255):'i',
(255,255,0):'o',
(128, 0, 128):'t',
(0,255,0):'s',
(255,0,0):'z',
(0,0,255):'j',
(255, 165, 0):'l',
#<----------------->
(48, 144, 109):'i',
(49, 127, 99):'i',
(57, 173, 131):'i',
(49, 143, 109):'i',
(55, 172, 130):'i',
(54, 168, 127):'i',
(49, 141, 108):'i',
(62, 186, 141):'i',
(57, 180, 134):'i',
(67, 195, 149):'i',
(63, 193, 146):'i',
(44, 230, 161):'i',
(63, 191, 144):'i',
(76, 207, 159):'i',
(80, 198, 156):'i',
(48, 127, 99):'i',
(48, 137, 106):'i',
(48, 144, 110):'i',

(193, 112, 63):'l',
(187, 109, 62): 'l',
(177, 101, 56):'l',
(195, 114, 64):'l',
(192, 113, 65):'l',
(179, 99, 50) :'l',
(177, 101, 54):'l',
(193, 114, 66):'l',
(184, 110, 49):'l',
(185, 104, 55):'l',
(174, 101, 57):'l',
(181, 101, 52):'l',
(183, 103, 53):'l',
(192, 112, 64):'l',
(174, 103, 58):'l',
(174, 102, 57):'l',
(174, 102, 58):'l',
(174, 100, 54):'l',
(180, 100, 51):'l',
(190, 115, 68):'l',
(182, 102, 52):'l',
(80, 62, 165):'j',
(80, 63, 165):'j',
(92, 75, 175):'j',
(82, 66, 160):'j',
(81, 64, 166):'j',
(83, 65, 167):'j' ,
(85, 69, 160):'j',
(95, 77, 178):'j',
(90, 74, 170):'j',
(86, 62, 210):'j',
(79, 61, 164):'j',
(85, 70, 162):'j',
(83, 67, 159):'j',
(93, 76, 178):'j', 
(96, 79, 179):'j',
(85, 70, 159):'j',
(82, 66, 159):'j',
(82, 65, 168):'j',
(78, 61, 164):'j',
 (96, 79, 175):'j',
(125, 111, 49):'o',
(182, 159, 60):'o',
(188, 163, 60):'o',
(194, 167, 55):'o',
(191, 166, 63):'o',
(190, 165, 62):'o',
(189, 166, 62):'o',
(206, 180, 75):'o',
(207, 181, 77):'o',  
(231, 194, 44):'o',
(204, 179, 74):'o',
(137, 120, 50):'o',
(176, 154, 59):'o',
(181, 158, 60):'o', 
(205, 180, 73):'o',
(185, 161, 61):'o',
(157, 137, 54):'o',
(125, 110, 48):'o',

(182, 54, 61):'z',
(192, 69, 76):'z',
(185, 68, 57):'z',
(183, 64, 58):'z',
(178, 55, 62):'z',
(186, 56, 63):'z',
(184, 55, 62):'z',
(175, 58, 65):'z',
(193, 65, 72):'z',
(180, 59, 65):'z',
(179, 51, 58):'z',
(197, 65, 72):'z',
(194, 67, 74):'z',
(194, 66, 73):'z',
(177, 57, 63):'z',
(181, 53, 60):'z',
(187, 62, 69):'z',
(176, 59, 65):'z',
(194, 64, 71):'z',
(175, 55, 61):'z',
(180, 52, 59):'z',

(143, 191, 62):'s',
(129, 173, 57):'s',
(139, 185, 61):'s',    
(164, 233, 47):'s',  
(131, 179, 50):'s',
(132, 177, 57):'s',
(143, 190, 64):'s',
(131, 176, 55):'s',
(132, 180, 51):'s', 
(131, 177, 54):'s',
(139, 179, 51):'s',
(136, 184, 55):'s',
(134, 183, 53):'s',
(142, 190, 63):'s',
(143, 191, 65):'s',
(128, 172, 56):'s',
(129, 173, 54):'s',
(134, 182, 53):'s',
(144, 190, 67):'s',
(133, 181, 52):'s',
(178, 79, 165):'t',
(169, 78, 138):'t',
(161, 66, 151):'t',
(168, 66, 159):'t',
(177, 77, 167):'t',
(159, 67, 150):'t',
(178, 79, 169):'t',
(177, 76, 168):'t',
(162, 69, 153):'t',
(164, 61, 154):'t', 
(212, 65, 197):'t',
(170, 74, 161):'t',
(167, 65, 157):'t',
(159, 69, 150):'t',
(178, 78, 168):'t',
(166, 64, 156):'t',
(159, 70, 150):'t',
(175, 75, 165):'t',
(175, 79, 165):'t',
(159, 66, 149):'t',
(168, 65, 158):'t',
(165, 62, 155):'t',
}

"""Colores correspondientes a las piezas de tetris."""

def calculate_distance(color1, color2):
    return np.sqrt(np.sum((np.array(color1) - np.array(color2))**2))
def determine_tetris_piece(captured_color, threshold=50):
    closest_piece = None
    min_distance = float('inf')
    
    for color, piece in tetris_colors.items():
        distance = calculate_distance(captured_color, color)
        if distance < min_distance:
            min_distance = distance
            closest_piece = piece
    
    if min_distance <= threshold:
        return closest_piece
    else:
        return "No Tetris piece recognized"
