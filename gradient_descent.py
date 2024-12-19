def gradient_descent(gradient, initial_x, learning_rate, num_iterations):
    x = initial_x
    history = [x]

    for _ in range(num_iterations):
        grad = gradient(x)
        x = x - learning_rate * grad
        history.append(x)

    return x, history


if __name__ == "__main__":
    # Пример использования функции
    def gradient(x):
        return 2 * x

    initial_x = 10
    learning_rate = 0.1
    num_iterations = 50

    optimal_x, history = gradient_descent(gradient, initial_x, learning_rate, num_iterations)

    print(f"Оптимальное значение x: {optimal_x}")
