def test_hash1():
  import almostUHM
  demo = almostUHM.generatePrecidualHashFunction(1234)
  hash = demo('Test String!')
  return '35725045e467693a5d24f86952dd881508824009ad2be8b1070c567aa6d448fc' == hash
  
