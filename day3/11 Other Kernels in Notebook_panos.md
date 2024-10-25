# How do I install other kernels for notebook?

## R Kernel

```bash
# 1. Update system packages:
sudo apt update && sudo apt upgrade -y

# 2. Install R:
sudo apt install r-base -y

# 3. Install IRkernel in R:
R

# 4. In the R console, run:
install.packages('IRkernel')
IRkernel::installspec(user = FALSE)

# 5. Exit R:
q()

# 6. Verify by launching Jupyter:
jupyter lab --ip=0.0.0.0 --no-browser
```

(Click on the link that starts with 127.0.0.)

In the R-notebook:

```R
# 1. Print a simple message
print("Hello, Jupyter with R!")

# 2. Create a sequence of numbers from 1 to 10
numbers <- 1:10
print(numbers)

# 3. Calculate the mean of a numeric vector
mean_value <- mean(numbers)
print(paste("The mean is:", mean_value))

# 4. Plot a simple graph
plot(numbers, main="Basic Line Plot", type="o", col="blue")

# 5. Create a simple data frame and display it
data <- data.frame(
  Name = c("John", "Jane", "Paul"),
  Age = c(23, 35, 28),
  Score = c(88, 92, 79)
)
print(data)

# 6. Summarize the data frame
summary(data)
```
---
## Octave Kernel

```bash
# 1. Update system packages:
sudo apt update && sudo apt upgrade -y

# 2. Install Octave:
sudo apt install octave -y

# 3. Install the Octave kernel:
pip install octave_kernel

# 4. Verify the kernel is installed:
jupyter kernelspec list

# 5. Launch Jupyter Notebook:
jupyter lab --ip=0.0.0.0 --no-browser
```
In Octave notebook

```octave
# 1. Print a simple message
disp("Hello, Jupyter with Octave!");

# 2. Create a matrix and display it
A = [1, 2, 3; 4, 5, 6; 7, 8, 9];
disp("Matrix A:");
disp(A);

# 3. Perform a matrix multiplication
B = A * A';
disp("Matrix multiplication result (A * A'):");
disp(B);

# 4. Plot a simple sine wave
x = linspace(0, 2 * pi, 100);
y = sin(x);
plot(x, y);
title("Sine Wave");
xlabel("x");
ylabel("sin(x)");

# 5. Solve a linear system of equations (Ax = b)
b = [1; 2; 3];
x = A \ b;
disp("Solution to Ax = b:");
disp(x);

```