const { expect } = require('chai');
const sinon = require('sinon');
const proxyquire = require('proxyquire');

describe('hello function', () => {
  it('should return a hello message with input', async () => {
    const event = { someKey: 'someValue' };

    // Falsificar la dependencia externa (puedes ajustar según tus necesidades)
    const externalDependencyMock = sinon.stub().resolves('Mocked result');

    // Utilizar proxyquire para reemplazar la dependencia en handler.js con el mock
    const { hello } = proxyquire('../handler', {
      './externalDependency': externalDependencyMock,
    });

    // Ejecutar la función con el evento y el mock de dependencia externa
    const result = await hello(event);

    // Realizar aserciones
    expect(result.statusCode).to.equal(200);
    expect(result.body).to.be.a('string');

    const body = JSON.parse(result.body);
    expect(body).to.have.property('message', 'Hola, mundo!');
    expect(body).to.have.property('input').deep.equal(event);

    // Asegurarse de que la dependencia externa se haya llamado con los parámetros correctos
    sinon.assert.calledOnce(externalDependencyMock);
    sinon.assert.calledWithExactly(externalDependencyMock, event.someKey);
  });
});
