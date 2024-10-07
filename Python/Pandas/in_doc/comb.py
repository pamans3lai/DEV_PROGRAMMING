{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "0af7f8d0-9efc-446a-a833-5c47de2765b0",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pandas'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[27], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pandas'"
     ]
    }
   ],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
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
      "Cell \u001b[0;32mIn[28], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m air_quality_no2 \u001b[38;5;241m=\u001b[39m \u001b[43mpd\u001b[49m\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mair_quality_no2_long.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m, parse_dates\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
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
   "execution_count": 32,
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
      "Cell \u001b[0;32mIn[32], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mair_quality_no2\u001b[49m\u001b[38;5;241m.\u001b[39mhead()\n",
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
   "execution_count": 30,
   "id": "4e893dee-d60f-4896-97a3-7814cc1b9451",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (719514810.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[30], line 2\u001b[0;36m\u001b[0m\n\u001b[0;31m    \"parameter\", \"value\"]]\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "\n",
    "#air_quality_no2 = air_quality_no2[[\"date.utc\", \"location\",\n",
    "                                   \"parameter\", \"value\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "685ab1f2-c8da-473e-a8a8-0924d54827b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/home/ai/DEV_PROGRAMMING/Python/Pandas/in_doc'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fcca48cd-678b-488f-9ba2-e8e935d6af42",
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
