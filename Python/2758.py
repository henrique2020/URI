import struct
# struct é necessário para resolver o problema de precisão dupla (float)
# para que se torne uma variável de precisão simples

a, b = map(float, input().split())
a = struct.unpack('f', struct.pack('f', a))[0]
b = struct.unpack('f', struct.pack('f', b))[0]
c, d = map(float, input().split())

#7. & 8.
print(f"A = {a:.6f}, B = {b:.6f}\nC = {c:.6f}, D = {d:.6f}")
#9. & 10.
print(f"A = {a:.1f}, B = {b:.1f}\nC = {c:.1f}, D = {d:.1f}")
#11. & 12.
print(f"A = {a:.2f}, B = {b:.2f}\nC = {c:.2f}, D = {d:.2f}")
#13. & 14.
print(f"A = {a:.3f}, B = {b:.3f}\nC = {c:.3f}, D = {d:.3f}")
#15. & 16.
print(f"A = {a:.3E}, B = {b:.3E}\nC = {c:.3E}, D = {d:.3E}")
#17. & 18.
print(f"A = {a:.0f}, B = {b:.0f}\nC = {c:.0f}, D = {d:.0f}")
