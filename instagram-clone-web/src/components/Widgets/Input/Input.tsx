import React, { Dispatch, FC, SetStateAction } from 'react'
import './Input.scss'

type Props = {
  placeholder?: string
  name?: string
  setChange: Dispatch<SetStateAction<string>>
}

const Input: FC<Props> = ({ placeholder, name, setChange }) => {
  return (
    <div className='input'>
      <input
        placeholder={placeholder}
        name={name}
        onChange={(e) => setChange(e.target.value)}
      />
    </div>
  )
}

export default Input
