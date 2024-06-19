import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import App from './App';
import UpdateClub from './components/updateClub';
import AddClubForm from './components/addClubForm';

test('Add Club Form', () => {
  const { getByLabelText, getByText } = render(<App />);
  const nameInput = getByLabelText(/Name:/i);
  const stadiumInput = getByLabelText(/Stadium:/i);
  const yearInput = getByLabelText(/Year:/i);
  const addButton = getByText(/Add New Club/i);

  expect(nameInput).toBeInTheDocument();
  expect(stadiumInput).toBeInTheDocument();
  expect(yearInput).toBeInTheDocument();
  expect(addButton).toBeInTheDocument();
});



test('updating a club', async () => {
  const mockClub = {
    id: 1,
    name: 'Mock Club',
    stadium: 'Mock Stadium',
    year: 2000
  };

  const mockUpdatedClub = {
    id: 1,
    name: 'Updated Club',
    stadium: 'Updated Stadium',
    year: '2022' // Updated to be a string
  };

  const mockUpdateClub = jest.fn();

  const { getByLabelText, getByText } = render(
    <UpdateClub onUpdateClub={mockUpdateClub} club={mockClub} />
  );

  const nameInput = getByLabelText('Name:');
  const stadiumInput = getByLabelText('Stadium:');
  const yearInput = getByLabelText('Year:');
  const updateButton = getByText('Update Club');

  fireEvent.change(nameInput, { target: { value: mockUpdatedClub.name } });
  fireEvent.change(stadiumInput, { target: { value: mockUpdatedClub.stadium } });
  fireEvent.change(yearInput, { target: { value: mockUpdatedClub.year } });
  fireEvent.click(updateButton);

  expect(mockUpdateClub).toHaveBeenCalledTimes(1);
  expect(mockUpdateClub).toHaveBeenCalledWith(mockUpdatedClub);
});


test('adding a club', () => {
  const mockAddClub = jest.fn();

  const { getByLabelText, getByText } = render(
    <AddClubForm onAddClub={mockAddClub} />
  );

  const nameInput = getByLabelText('Name:');
  const stadiumInput = getByLabelText('Stadium:');
  const yearInput = getByLabelText('Year:');
  const addButton = getByText('Add New Club');

  const newClub = {
    name: 'New Club',
    stadium: 'New Stadium',
    year: '2024'
  };

  fireEvent.change(nameInput, { target: { value: newClub.name } });
  fireEvent.change(stadiumInput, { target: { value: newClub.stadium } });
  fireEvent.change(yearInput, { target: { value: newClub.year } });
  fireEvent.click(addButton);

  expect(mockAddClub).toHaveBeenCalledTimes(1);
  expect(mockAddClub).toHaveBeenCalledWith(newClub);
});