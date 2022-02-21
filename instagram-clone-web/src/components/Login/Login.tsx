import React, { Dispatch, FC, SetStateAction, useRef, useState } from 'react'

import Button from '../Widgets/Button'
import Input from '../Widgets/Input/Input'
import './Login.scss'
import { selectUser, loginAsync } from '../../features/auth/authSlice'
import { useAppSelector, useAppDispatch } from '../../app/hooks'

type Props = {
  closeModal: (isOpen: boolean) => void
}

const Login: FC<Props> = ({ closeModal }) => {
  const [username, setUsername] = useState<string>('')
  const [password, setPassword] = useState<string>('')

  const dispatch = useAppDispatch()

  const onSubmit = async (e: any) => {
    e.preventDefault()

    let formData = new FormData()
    formData.append('username', username)
    formData.append('password', password)
    await dispatch(loginAsync(formData))
    closeModal(false)
  }
  return (
    <form className='login' name='login' onSubmit={onSubmit}>
      {/* <div className='header'>
        <Logo />
      </div> */}
      <div className='body'>
        <Input placeholder='Username' name='username' setChange={setUsername} />
        <Input placeholder='Password' name='password' setChange={setPassword} />
      </div>
      <div className='actions'>
        <Button primary type='submit'>
          Login
        </Button>
      </div>
    </form>
  )
}

export default Login
