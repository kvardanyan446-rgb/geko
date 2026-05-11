const transactions = [
    { id: "T001", info: "  apple.com/bill  ", amount: "1200.50 USD", date: "2023-10-01" },
    { id: "T002", info: "Sberbank Transfer", amount: "5000.00 RUB", date: "2023-10-01" },
    { id: "T003", info: "APPLE.COM/BILL", amount: "1200.50 USD", date: "2023-10-01" }, 
    { id: "T004", info: " Netflix Subscription ", amount: "15.99 USD", date: "2023-10-02" },
    { id: "T005", info: "Amazon Web Services", amount: "450.00 USD", date: "2023-10-03" },
    { id: "T006", info: "Apple.com/bill", amount: "30.00 USD", date: "2023-10-04" }
];


const cleaned = transactions.map(t => ({
    ...t,
    info: t.info.trim().toLowerCase()
}));

console.log(cleaned);



 amount = "1200.50 USD";
amount.split("");
parseFloat("1200.50");
result = {
  value: 1200.5,
  currency: "USD"
}
console.log(result)



amount = "5000.00 RUB";
amount.split("");
parseFloat("5000.50");
result = {
    value:5000.50,
    currency: "RUB"
}
console.log(result);



amount = "1200.50 USD"
amount.split("");
parseFloat("1200.50");
result = {
    value:1200.50,
    currency: "USD"
}
console.log(result);



amount = "15.99USD"
amount.split("");
parseFloat(15.99);
result = {
    value: 15.99,
    currency: "USD"
}
console.log(result);




amount = "450.00 USD"
amount.split("");
parseFloat(450.00);
result = {
    value: 450.00,
    currency: "USD"
}
console.log(result);



amount = "30.00 USD"
amount.split("");
parseFloat(30.00);
result = {
    value: 30.00,
    currency: "USD"
}
console.log(result);
