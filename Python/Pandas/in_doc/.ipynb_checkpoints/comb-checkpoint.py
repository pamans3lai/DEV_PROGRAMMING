{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0af7f8d0-9efc-446a-a833-5c47de2765b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6b5fa917-3b4d-4092-a7dc-cf5c7e76a826",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[7], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m air_quality_no2 \u001b[38;5;241m=\u001b[39m \u001b[43mpd\u001b[49m\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mair_quality_no2_long.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m, parse_dates\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "air_quality_no2 = pd.read_csv(\"air_quality_no2_long.csv\", parse_dates=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e893dee-d60f-4896-97a3-7814cc1b9451",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "air_quality_no2 = air_quality_no2[[\"date.utc\", \"location\",\n",
    "                                   \"parameter\", \"value\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "207c319f-0a6c-4ab3-8d0f-4070932a15fa",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'air_quality_no2' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[8], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mair_quality_no2\u001b[49m\u001b[38;5;241m.\u001b[39mhead()\n",
      "\u001b[0;31mNameError\u001b[0m: name 'air_quality_no2' is not defined"
     ]
    }
   ],
   "source": [
    "air_quality_no2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "685ab1f2-c8da-473e-a8a8-0924d54827b7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
