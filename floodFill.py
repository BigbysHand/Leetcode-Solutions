class Solution(object):
  def fill(self, image, sr, sc, target, color):
    if (sr < 0 or sr >= len(image)) or (sc < 0 or sc >= len(image[0])) or (image[sr][sc] == color):
        return
    if target != image[sr][sc]:
        return
    image[sr][sc] = color

    self.fill(image, sr-1, sc, target, color)
    self.fill(image, sr+1, sc, target, color)
    self.fill(image, sr, sc-1, target, color)
    self.fill(image, sr, sc+1, target, color)

  def floodFill(self, image, sr, sc, color):

    target = image[sr][sc]
    self.fill(image, sr, sc, target, color)
    return image