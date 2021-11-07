def spinning_rings(inner_max, outer_max):
    i, o, m = 0, 0, 0

    for x in range(1000000):
        i = i - 1 if (i > 0) else inner_max
        o = o + 1 if (o < outer_max) else 0
        m += 1
        # print("m", m, "i(", i, o, ")o")
        if i == o:

            return m

import time

def main():
  tests = 1
  start_time = time.time()
  for a in range(tests):

      assert (spinning_rings(2, 3)) == 5
      print (spinning_rings(2, 10))
      # print (spinning_rings(3, 2))
      # print (spinning_rings(5, 2))
      print (spinning_rings(2, 5))
      # print (spinning_rings(10, 3))
      print (spinning_rings(3, 22))
      print (spinning_rings(4, 21))

  print("--- %s seconds ---" % (time.time() - start_time))

  start_time = time.time()
  for a in range(tests):

      # assert (spinning_rings(24688025040812, 112804577778109)) == 5

      spinning_rings(24688025040812, 112804577778109)

  print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
  main()