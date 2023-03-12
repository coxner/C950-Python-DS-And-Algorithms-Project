
I) The biggest advantage of the nearest neighbor algorithm is the simplicity of it. There are only two process that
take place the calculating of distance and finding the nearest neighbor based off comparisons with other packages. The code
is fairly easy to follow and can be understood and picked up easily. It's an algorithm that can easily adjust to increasing
and decreasing inputs to without any adjustments to code being needed.

Two algorithms we could use instead of the one in the project is a simple min value algorithm. We could calculate the
distance for each package assign it to the package and loop through all packages until we find the minimum one instead of
using two pointers.  Another approach would be to use a sort algorithm that arranges all the packages on the truck
from the lowest distance to the highest distance. From sorting the packages on the truck we can loop through and deliver
each package.

J) If I did this project again I would try to solve the problem of manually loading the trucks. I would try to come up
with a algorithm to load the trucks with packages. This would be hard to do as there is alot of conditions that would need
to be assigned to each individual package. These conditions would all have to be met in the loading of the packages onto the
truck to.

K) The search function of the hash table loops through all the elements in the hash table and returns a element if the
key matches. Therefore, it has a run tim of O(n) so any element added to the hash map will increase its run time by n.

b) The space complexity of the hash map is also O(n) adding packages would just increase the size of the hash map by n.
Working with packages making storing packages easy as each package should have a unique id which all leads to no
collisions needing to be handled. (Iyer 2021)

c) If another city was added the lookup time of the data structure would remain the same the lookup time would still be
O(n). The space usage would change however because with the addition of an addition city the data structure will now have to
handle collisions. With collisions now being handled the space complexity changes from O(n) to O(n+m).

2) Two other data structures we could use instead of a hash map is a min heap and a stack. If we had a min heap we could
just traverse the data structure by the lowest distance value and deliver that package.(Khawaja 2021) If we used a stack we could come
up with a recursive algorithm that would keep calling as long as there is packages to deliver. We would place the package
with the longest distance on the bottom of the stack. Once the stack is full the packages with the shortest distance will
be on top and we can deliver packages from there.


Sources:

How take user input in time format HH:Mm in python language: Sololearn: Learn to code for free! Sololearn. (n.d.).
Retrieved February 4, 2023, from https://www.sololearn.com/discuss/2278289/how-take-user-input-in-time-format-hh-mm-in-python-language

Iyer, J. V. (2021, December 6). Time and space complexity of hash table operations.
OpenGenus IQ: Computing Expertise &amp; Legacy. Retrieved February 4, 2023, from https://iq.opengenus.org/time-complexity-of-hash-table/

Two pointers. LeetCode. (n.d.). Retrieved February 4, 2023,
from https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4501/

Khawaja, M. F. (2021, August 14). Heaps vs. stacks: What sets them apart? MUO. Retrieved February 16, 2023,
from https://www.makeuseof.com/heaps-vs-stacks/


