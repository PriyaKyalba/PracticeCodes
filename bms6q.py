#WAP to find the sum of all prime below two million

is_prime = [True] * 2000000
is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
sum = 0
for num in range(2, 2000000):
    if is_prime[num]:
        sum += num
        for multiple in range(num * 2, 2000000, num):
            is_prime[multiple] = False

print(f"The sum of all primes below {200000} is: {sum}")
