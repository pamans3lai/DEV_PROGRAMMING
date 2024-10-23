def residue_gaps(pm)
  primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
  i = primes.index(pm)
  modpn = primes[0..i].reduce :*          # modulus is primorial pm#
  res_gaps = Hash.new(0)                  # create hash of residue gaps
  res_gaps[2] = 1; res_gaps[4] = 1        # initial gap counts of 2 and 4
  r1, r2 = 1, 2 + pm                      # initial first two residues
  while r2 < modpn / 2                    # for first half modulus residues
    if r2.gcd(modpn) == 1                 # if r2 is a residue
      res_gaps[r2 - r1] += 2              # compute gap size, double cnt for mirror pair
      r1 = r2                             # set old residue to current residue
    end
    r2 += 2                               # set next odd value to current residue
  end
  res_gaps.to_a.sort!                     # output array of [gap size, gap count]
end

pm   = ARGV[0].to_i                       # read prime value from terminal
print residue_gaps(pm)                    # display array of ai gap values
puts
