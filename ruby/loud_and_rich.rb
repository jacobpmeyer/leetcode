# @param {Integer[][]} richer
# @param {Integer[]} quiet
# @return {Integer[]}

# Return an integer array answer where answer[x] = y if y is the least quiet
# person (that is, the person y with the smallest value of quiet[y]) among all
# people who definitely have equal to or more money than the person x.

# Input:
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
# person 0 has quiet of 3

# Output: [5,5,2,5,4,5,6,7]


# Note before done: this may be best solved with a linked list
def loud_and_rich(richer, quiet)
  h = Hash.new { |h, k| h[k] = Set.new }
  richer.each do |r|
    h[r[0]] << r[1]
    h[r[0]].merge(h[1])
  end
  h.each do |k, v|
    k
  end
  k = h.keys.sort { |a, b| b <=> a }

end
