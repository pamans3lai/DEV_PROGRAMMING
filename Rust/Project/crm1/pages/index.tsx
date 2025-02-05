import { useState, useEffect } from 'react';
import { useStore } from '../store';

function CustomerList() {
  const store = useStore();
  const customer = store.getState().customers;

  return (
    <div>
      <h1>Customer List</h1>
      <ul>
        {customers.map((customer) => (
          <li key={customer.id}>{customer.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default CustomerList;
