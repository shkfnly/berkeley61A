def code_switcher(stri):
  results = []
  for elem in stri:
    i = 0
    if elem in dicta:
      while i < len(dicta):
        if elem == dicta[i]:
          if (i + 2) >= len(dicta):
            results.append(dicta[(i + 2) - len(dicta)])
            break  
          results.append(dicta[i + 2])
          break
        i += 1
    else:
      results += elem
  s = ''.join(results)
  return s
       
stringy = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
dicta = [ "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z" ]

code_switcher(stringy)