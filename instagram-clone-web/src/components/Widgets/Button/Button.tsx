import React, { FC } from 'react'
import './Button.scss'

type Props = {
  children: any
  primary?: boolean
  onClick?: () => void
  type?: 'button' | 'submit' | 'reset' | undefined
}

const Button: FC<Props> = ({ children, primary, onClick, type = 'button' }) => {
  return (
    <button
      className={`button ${primary ? 'primary' : ''}`}
      onClick={onClick}
      type={type}
    >
      {children}
    </button>
  )
}

export default Button
