const orders = [
  { id: 1, user: "Ivan", items: [{ name: "Laptop", price: 1200, qty: 1 }, { name: "Mouse", price: 25, qty: 2 }], status: "pending", createdAt: "2026-04-28" },
  { id: 2, user: "Anna", items: [{ name: "Phone", price: 800, qty: 1 }], status: "completed", createdAt: "2026-04-20" },
  { id: 3, user: "Ivan", items: [{ name: "Keyboard", price: 100, qty: 1 }], status: "pending", createdAt: "2026-04-29" }
];


const calculateOrderTotal = (order) => 
  order.items.reduce((sum, item) => sum + item.price * item.qty, 0);


const getUserPendingOrders = (orders, username) => 
  orders.filter(order => order.user === username && order.status === "pending");


const getTotalRevenue = (orders) => 
  orders
    .filter(order => order.status === "completed")
    .reduce((total, order) => total + calculateOrderTotal(order), 0);


const groupOrdersByUser = (orders) => 
  orders.reduce((acc, order) => {
    if (!acc[order.user]) acc[order.user] = [];
    acc[order.user].push(order);
    return acc;
  }, {});


const getTopUsers = (orders, topN) => {
  const userTotals = orders.reduce((acc, order) => {
    const amount = order.status === "completed" ? calculateOrderTotal(order) : 0;
    acc[order.user] = (acc[order.user] || 0) + amount;
    return acc;
  }, {});

  return Object.keys(userTotals)
    .map(name => ({ user: name, total: userTotals[name] }))
    .sort((a, b) => b.total - a.total)
    .slice(0, topN);
};

console.log("1. Order 1 Total:", calculateOrderTotal(orders[0]));
console.log("2. Ivan's Pending:", getUserPendingOrders(orders, "Ivan"));
console.log("3. Total Revenue:", getTotalRevenue(orders));
console.log("4. Grouped Orders:", groupOrdersByUser(orders));
console.log("5. Top Users:", getTopUsers(orders, 2));