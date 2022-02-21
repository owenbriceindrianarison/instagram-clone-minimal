import React, { FC, ReactElement } from 'react'
import './Modal.scss'

type Props = {
  title?: FC<any> | ReactElement<any>
  open: boolean
  onClose: (isOpen: boolean) => void
  children: any
}

const Modal: FC<Props> = ({ title, open = false, onClose, children }) => {
  return (
    <div className={`modal ${open ? 'is-open' : ''}`}>
      <div className='modal-content'>
        <div className='modal-header'>
          {title}
          <span className='close' onClick={() => onClose(false)}>
            &times;
          </span>
        </div>
        <div className='modal-body'>{children}</div>
      </div>
    </div>
  )
}

export default Modal
